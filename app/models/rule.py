from pydantic import BaseModel, field_validator
from typing import Optional, Literal

class Node(BaseModel):
    type: Literal["operator", "operand"]
    value: str
    left: Optional['Node'] = None
    right: Optional['Node'] = None

    @field_validator('left', 'right')
    def check_children(cls, v, info):
        if info.data.get('type') == 'operator' and v is None:
            raise ValueError("Operator nodes must have both left and right children")
        if info.data.get('type') == 'operand' and v is not None:
            raise ValueError("Operand nodes cannot have children")
        return v

    model_config = {
        "arbitrary_types_allowed": True
    }