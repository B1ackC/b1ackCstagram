from flask import Flask, render_template, request, redirect, session
import os
from src.data.format import PostInputDto, UserInputDto
from src.db.db import DBuser

app = Flask(__name__, static_folder='static')
# app.secret_key = os.urandom(24)
# posts = []

#
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# # 파일 허용
# def allow_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#
# # method: GET / 로그인
# @app.get('/')
# def getLogin():
#     return render_template('login.html')

# method: POST / 로그인
# request: userId, userPassword
@app.post('/')
def postLogin():
    # user = user_login(request)

    # if(user is not False):
    #     session['userId'] = user.userId
    #     return redirect('/board')

    return redirect('/')

@app.get('/register')
def getRegister():
    return render_template('join.html')

@app.post('/register')
def postRegister():
    loginInfo = UserInputDto.requestFrom(request)


    if DBuser().add_user_from_dto(loginInfo):
        return redirect('/')
    else:
        return redirect('/register')
#게시글 작성
# @app.get('/post')
# def getPosts():
#     return render_template('post.html')

# @app.post('/post')
# def insertPosts():
#     postInfo = PostInputDto.requestForm(request)
#     if post_insert(postInfo):
#         global posts
#         contentTitle = request.form.get('title')
#         contentText = request.form.get('content')
#         imageFile = request.files['file']
#
#         if imageFile and allow_file(imageFile.filename):
#             filename = imageFile.filename
#             filepath = os.path.join('static/upload', imageFile.filename)
#             imageFile.save(filepath)
#         else:
#             filename = None
#         # 배열 데이터 삽입
#         posts.append({
#             'number': len(posts) + 1,
#             'title': contentTitle,
#             'context': contentText,
#             'fileName': filename
#         })
#         return redirect('/board')

#게시글 보기
# @app.get('/board')
# def getBoard():
#     userId = session.get('userId')
#     return render_template('board.html', posts=posts, userId=userId)
#
# @app.post('/board')
# def searchPost():
#     global posts
#     search_term = request.form.get('search')
#     if search_term:
#         filtered_posts = [post for post in posts if search_term in post['title']]
#         return render_template('board.html', posts=filtered_posts)
#     return render_template('board.html', posts=posts)
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=8080, debug=True)