from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class User(BaseModel):
    username: str
    usermail: EmailStr
    userpassword: str


class UserPublic(BaseModel):
    id: int
    username: str
    usermail: EmailStr


class UserDB(User):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
