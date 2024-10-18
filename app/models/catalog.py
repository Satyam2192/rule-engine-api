from pydantic import BaseModel
from typing import Dict, Any, Union, List

class AttributeCatalog(BaseModel):
    attributes: Dict[str, Dict[str, Union[str, List[str], int, float]]]

catalog = AttributeCatalog(
    attributes={
        "age": {"type": "int", "min": 0, "max": 120},
        "department": {"type": "str", "allowed": ["Sales", "Marketing", "Engineering"]},
        "salary": {"type": "float", "min": 0},
        "experience": {"type": "int", "min": 0},
    }
)

def validate_attribute(name: str, value: Any) -> bool:
    if name not in catalog.attributes:
        return False
    
    attr_info = catalog.attributes[name]
    if attr_info["type"] == "int":
        return isinstance(value, int) and attr_info["min"] <= value <= attr_info["max"]
    elif attr_info["type"] == "float":
        return isinstance(value, (int, float)) and value >= attr_info["min"]
    elif attr_info["type"] == "str":
        return isinstance(value, str) and value in attr_info["allowed"]
    
    return False