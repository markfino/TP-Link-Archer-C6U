from dataclasses import dataclass

@dataclass
class ACLEntry:
    name: str
    mac: str