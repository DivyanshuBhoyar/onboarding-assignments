from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str

admin = User("00", "The only user")