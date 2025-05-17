from dataclasses import dataclass

from globals import Actions

@dataclass
class RouterCmds:
    short: str
    long: str
    action: Actions
    desc: str