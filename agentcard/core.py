# agentcard/core.py
from pydantic import BaseModel, Field
import yaml

class AgentCard(BaseModel):
    id: str
    name: str
    purpose: str
    memory: dict
    tools: list
    observability: dict
    governance: dict

    @classmethod
    def from_yaml(cls, path: str):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def register_to_phoenix(self):
        # pseudo-API call to Phoenix tracing metadata
        print(f"Registered agent {self.id} with Phoenix observability.")

