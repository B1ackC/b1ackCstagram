from dataclasses import dataclass
from flask import session


@dataclass
class users:
    userId: str #= Field(min_length=4, max_length=20)
    userPassword: str #= Field(..., max_length=20, min_length=4)
    userName: str


@dataclass
class PostInputDto:
    number: int
    title: str
    context: str
    fileName: str
    userid: str
    #views: int
    #like: int
    #createDate: str

    @staticmethod
    def requestForm(request):
        title = request.form.get('title')
        context = request.form.get('context')
        fileName = request.form.get('fileName')
        userid = session.get('userId')
        return PostInputDto(title=title, context=context, fileName=fileName, userid=userid)


@dataclass
class UserInputDto:
    userId: str
    userPassword: str
    userName: str

    @staticmethod
    def requestFrom(request):
        userId = request.form.get('userId')
        userPassword = request.form.get('userPassword')
        userName = request.form.get('userName')
        return UserInputDto(userId=userId, userPassword=userPassword, userName=userName)

