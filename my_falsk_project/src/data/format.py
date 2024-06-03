from dataclasses import dataclass

@dataclass
class users:
    userId: str
    userPassword: str
    userName: str

@dataclass
class posts:
    number: int
    title: str
    context: str
    fileName: str
