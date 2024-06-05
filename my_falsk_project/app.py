from flask import Flask, render_template, request, redirect
import random, os
from src.data.format import users, posts
from src.data.db import DBcreate

app = Flask(__name__, static_folder='static')
posts = []
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


#파일 읽기 
def load_texts(filename):
    with open(filename, 'r') as file:
        texts = file.readlines()
    # 각 줄 끝의 줄바꿈 문자를 제거
    texts = [text.strip() for text in texts]
    return texts

# 랜덤 이미지 불러오기
def get_random_image(directory):
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return random.choice(image_files)

# 파일 업로드, 확장자 검증
def allow_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#랜덤 이미지 출력
@app.get('/main')
def main():
    texts = load_texts('static/texts.txt')
    random_text = random.choice(texts)
    random_image = get_random_image('static/image')
    return render_template('main.html', random_text=random_text, image_file=f"image/{random_image}")

#이미지 1~5
@app.get('/random/<int:image_id>')
def random_image(image_id):
    image_file = f"image/{image_id}.png"
    texts = load_texts('static/texts.txt')
    random_text = texts[image_id - 1]
    return render_template('main.html', random_text=random_text, image_file=image_file)

#로그인
@app.get('/')
def getLogin():
    return render_template('login.html')

@app.post('/')
def postLogin():
    userId = request.form.get('userId')
    userPassword = request.form.get('userPassword')
    for user in users:
        if user['userId'] == userId and user['userPassword'] == userPassword:
            return redirect('/main')
    return redirect('/')

#회원가입
@app.get('/register')
def getRegister():
    return render_template('join.html')

@app.post('/register')
def postRegister():
    userId = request.form.get('userId')
    userPassword = request.form.get('userPassword')
    userName = request.form.get('userName')
    # DB 데이터 insert
    DBcreate().add_user(userId, userPassword, userName)
    return redirect('/post')
#게시글 작성
@app.get('/post')
def getPosts():
    return render_template('post.html')

@app.post('/post')
def insertPosts():
        global posts
        contentTitle = request.form.get('title')
        contentText = request.form.get('content')
        imageFile = request.files['file']
        
        if imageFile and allow_file(imageFile.filename):
            filename = imageFile.filename
            filepath = os.path.join('static/upload', imageFile.filename)
            imageFile.save(filepath)
        else:
            filename = None
        # 배열 데이터 삽입
        posts.append({
            'number': len(posts) + 1,
            'title': contentTitle,
            'context': contentText,
            'fileName': filename
        })
        return redirect('/board')

#게시글 보기
@app.get('/board')
def getBoard():
    return render_template('board.html', posts=posts)

@app.post('/board')
def searchPost():
    global posts
    search_term = request.form.get('search')
    if search_term:
        filtered_posts = [post for post in posts if search_term in post['title']]
        return render_template('board.html', posts=filtered_posts)
    return render_template('board.html', posts=posts)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)