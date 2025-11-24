from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class Preset:
    id: int
    name: str
    description: str | None
    filter_definition: Dict[str, Any]
