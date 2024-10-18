import ast
import operator
from typing import List, Dict, Any
from ..models.rule import Node
from ..models.catalog import validate_attribute

def create_rule(rule_string: str) -> ast.AST:
    rule_string = rule_string.replace("AND", "and").replace("OR", "or")
    
    try:
        tree = ast.parse(rule_string, mode='eval')
        return parse_ast_node(tree.body)  
    except SyntaxError as e:
        raise ValueError(f"Invalid rule syntax: {str(e)}")


def parse_ast_node(node) -> Node:
    if isinstance(node, ast.BoolOp): 
        return Node(
            type="operator",
            value="AND" if isinstance(node.op, ast.And) else "OR",
            left=parse_ast_node(node.values[0]),
            right=parse_ast_node(node.values[1])
        )
    elif isinstance(node, ast.Compare): 
        left = node.left.id if isinstance(node.left, ast.Name) else node.left.value
        right = node.comparators[0].value if isinstance(node.comparators[0], ast.Constant) else node.comparators[0].id
        op = type(node.ops[0]).__name__
        return Node(type="operand", value=f"{left} {op} {right}")
    else:
        raise ValueError(f"Unsupported node type: {type(node)}")



def combine_rules(rules: List[Node]) -> Node:
    if not rules:
        return None
    if len(rules) == 1:
        return rules[0]
    return Node(type="operator", value="OR", left=rules[0], right=combine_rules(rules[1:]))

def evaluate_rule(node: Node, data: Dict[str, Any]) -> bool:
    if node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == "OR":
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
    elif node.type == "operand":
        left, op, right = node.value.split()

        if not validate_attribute(left, data.get(left)):
            raise ValueError(f"Invalid attribute: {left}")

        left_value = data.get(left, left)

        if right.isnumeric():
            right_value = int(right)
        else:
            right_value = right.strip('"')

        op_map = {
            "Gt": operator.gt,
            "Lt": operator.lt,
            "Eq": operator.eq,
            "GtE": operator.ge,
            "LtE": operator.le,
            "NotEq": operator.ne
        }

        if op not in op_map:
            raise ValueError(f"Invalid operator: {op}")

        return op_map[op](left_value, right_value)


def modify_rule(node: Node, path: List[str], new_value: str) -> Node:
    if not path:
        if node.type == "operand":
            return Node(type="operand", value=new_value)
        else:
            raise ValueError("Cannot modify an operator node directly")

    current, *remaining = path
    if current == "left":
        return Node(type=node.type, value=node.value, left=modify_rule(node.left, remaining, new_value), right=node.right)
    elif current == "right":
        return Node(type=node.type, value=node.value, left=node.left, right=modify_rule(node.right, remaining, new_value))
    else:
        raise ValueError(f"Invalid path: {current}")