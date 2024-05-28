from flask import Flask, render_template, request, redirect

import random
import os

app = Flask(__name__, static_folder='static')

users = []
posts = []


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
        

@app.route('/main')
def main():
    texts = load_texts('static/texts.txt')
    random_text = random.choice(texts)
    random_image = get_random_image('static/image')
    return render_template('main.html', random_text=random_text, image_file=f"image/{random_image}")


@app.route('/random/<int:image_id>')
def random_image(image_id):
    image_file = f"image/{image_id}.png"
    texts = load_texts('static/texts.txt')
    random_text = texts[image_id - 1]
    return render_template('main.html', random_text=random_text, image_file=image_file)

@app.route('/', methods=['GET', 'POST'])
def userLogin():
    # TODO: 로그인 기능 구현
    if request.method == 'GET':
        return render_template("login.html")
    else:
        userId = request.form.get("userId")
        userPassword = request.form.get('userPassword')
        for user in users:
            if user['userId'] == userId and user['userPassword'] == userPassword:
                return redirect('/main')
        return redirect('/')


@app.route('/register', methods=['GET','POST'])
def registerUser():
    if request.method == 'GET':
        return render_template("join.html")
    else:
        userId = request.form.get('userId')
        userPassword = request.form.get('userPassword')
        userName = request.form.get('userName')
        # 값 받아오는지 확인
        users.append({
             'userId': userId,
             'userPassword': userPassword,
             'userName': userName
        })

        print(users)
        # 추후 DB 연동
        return redirect('/post')
    
@app.route('/post', methods=['GET', 'POST'])
def postContent():
    contentNumber = 0
    if request.method == 'GET':
        return render_template('post.html')
    elif request.method == 'POST':
        contentNumber += 1
        contentTitle = request.form.get('title')
        contentText = request.form.get('content')
        imageFile = request.files['file']

        if imageFile:
            # Save the file to the static/uploads directory
            # filename = imageFile.filename
            filename = imageFile.filename
            # filepath = os.path.join('static/uploads', filename)
            # imageFile.save(filepath)
        else:
            filename = None
        posts.append({
            'number': contentNumber,
            'title': contentTitle,
            'context': contentText,
            'fileName': filename
        })
        return redirect('/board')
    else:
        return redirect('/post')

@app.route('/board', methods=['GET', 'POST'])
def board():
    if request.method == 'GET':
        return render_template('board.html', posts=posts)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)