# from flask import Flask, render_template, redirect, request, url_for
# import random

# app = Flask(__name__)
# # app.run('0.0.0.0',port=8080,defug=True)
# # @app.route('/test')
# # def test():
# 	# return render_template(image_file="image/1.png")
# 	# return 'New Page'

# # @app.route('/test2', methods=['GET','POST'])
# # def test2():
# # 	if request.method == 'POST':
# # 		return redirect(url_for('main'))
# 	# return render_template('main.html')
# 	# return render_template(image_file="image/1.png")

# def load_texts(filename):
# 	with open(filename, 'r') as file:
# 		texts = file.read()
# 		# texts = [text.strip() for texts in txt_file]
# 	return texts

# @app.route('/')
# def index():
# 	return 'This is Home!'

# @app.route('/test1')
# def index2():
# 	# image_path = 'image/1.png'
# 	texts = load_texts('static/texts.txt')
# 	# random_text = random.choice(texts)
# 	return render_template('main.html', texts=texts, image_file="static/image/1.png")\
	
# @app.route('/test2')
# def index3():
# 	return 'test2'

# @app.route('/random/1')
# def image1():
# 	return render_template('main.html', image_file="image/1.png")

# @app.route('/random/2')
# def image2():
# 	return render_template('main.html', image_file="image/2.png")

# @app.route('/random/3')
# def image3():
# 	return render_template('main.html', image_file="image/3.png")

# @app.route('/random/4')
# def image4():
# 	return render_template('main.html', image_file="image/4.png")

# @app.route('/random/5')
# def image5():
# 	return render_template('main.html', image_file="image/4.png")



)
from flask import Flask, render_template, request, redirect

import random
import os

app = Flask(__name__, static_folder='static')

def load_texts(filename):
    with open(filename, 'r') as file:
        texts = file.readlines()
    # 각 줄 끝의 줄바꿈 문자를 제거
    texts = [text.strip() for text in texts]
    return texts

def get_random_image(directory):
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return random.choice(image_files)

@app.route('/', methods=['GET','POST'])
def userLogin():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		userId = request.form.get("userId")
		userPassword = request.form.get('userPassword')
		print(userId)
		print(userPassword)
		return redirect('/')
        

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

@app.route('/register', methods=['GET','POST'])
def registerUser():
    if request.method == 'GET':
        return render_te  Pmplate("join.html")
    else:
        userId = request.form.get('userId')
        userPassword = request.form.get('userPassword')
        userName = request.form.get('userName')
        # 값 받아오는지 확인
        print(userId)
        print(userPassword)
        print(userName)
        # 추후 DB 연동
        return redirect('/')
    
@app.route('/post', methods=['GET','POST'])
def postContent():
    if request.method == 'GET':
     return render_template('post.html')
    elif request.method == 'POST':
         contentTitle = request.form.get('title')
         contentText = request.form.get('content')
         imageFile = request.files['file']
         print(contentTitle)
         print(contentText)
         print(imageFile)
         return redirect('/post')
    else:
         return redirect('/post')

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)