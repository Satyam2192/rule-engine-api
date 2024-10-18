from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from ..services.rule_engine import create_rule, combine_rules, evaluate_rule, modify_rule
from ..models.rule import Node

router = APIRouter()

class RuleRequest(BaseModel):
    rule_string: str

class EvaluateRequest(BaseModel):
    ast: Node
    data: Dict[str, Any]

class ModifyRuleRequest(BaseModel):
    ast: Node
    path: List[str]
    new_value: str

@router.post("/rules")
async def create_rule_api(request: RuleRequest):
    try:
        rule_ast = create_rule(request.rule_string)
        return rule_ast
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/combine_rules")
async def combine_rules_api(rules: List[Node]):
    combined_ast = combine_rules(rules)
    return combined_ast

@router.post("/evaluate_rule")
async def evaluate_rule_api(request: EvaluateRequest):
    result = evaluate_rule(request.ast, request.data)
    return {"result": result}

@router.post("/modify_rule")
async def modify_rule_api(request: ModifyRuleRequest):
    modified_ast = modify_rule(request.ast, request.path, request.new_value)
    return modified_ast