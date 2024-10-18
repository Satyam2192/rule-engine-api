import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.rule_engine import create_rule, combine_rules, evaluate_rule, modify_rule
from app.models.rule import Node

def test_create_rule():
    rule1 = '((age > 30 AND department == "Sales") OR (age < 25 AND department == "Marketing")) AND (salary > 50000 OR experience > 5)'
    ast1 = create_rule(rule1)
    assert ast1.type == "operator"
    assert ast1.value == "AND"
    
    rule2 = '((age > 30 AND department == "Marketing")) AND (salary > 20000 OR experience > 5)'
    ast2 = create_rule(rule2)
    assert ast2.type == "operator"
    assert ast2.value == "AND"


def test_combine_rules():
    rule1 = create_rule("age > 30")
    rule2 = create_rule("salary > 50000")
    combined = combine_rules([rule1, rule2])
    assert combined.type == "operator"
    assert combined.value == "OR"
    assert combined.left == rule1
    assert combined.right == rule2

def test_evaluate_rule():
    rule = create_rule('(age > 30 AND department == "Sales") OR salary > 50000')
    data1 = {"age": 35, "department": "Sales", "salary": 45000}
    assert evaluate_rule(rule, data1) == True
    
    data2 = {"age": 25, "department": "Marketing", "salary": 55000}
    assert evaluate_rule(rule, data2) == True
    
    data3 = {"age": 25, "department": "Marketing", "salary": 45000}
    assert evaluate_rule(rule, data3) == False

def test_modify_rule():
    rule = create_rule("age > 30 AND salary > 50000")
    modified = modify_rule(rule, ["left"], "age > 35")
    assert modified.left.value == "age > 35"

def test_invalid_rule():
    with pytest.raises(ValueError):
        create_rule("age >") 

def test_attribute_validation():
    rule = create_rule('age > 30 AND department == "Marketing"')
    data = {"age": 35, "department": "Marketing"}
    assert evaluate_rule(rule, data) == True


def custom_function(x):
    return x * 2

def test_user_defined_function():
    pass