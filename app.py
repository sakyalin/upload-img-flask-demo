from flask import Flask
from flask import request, render_template, redirect, url_for
import os

basedir = os.path.abspath(os.path.dirname(__file__))
photo_path = os.path.join("static", "photo")

app = Flask(__name__)


@app.route('/')
def index_home():
    path = os.path.join(basedir, photo_path)
    # 转成静态路径
    photos = [os.path.join(photo_path, item) for item in os.listdir(path)]
    return render_template('index.html', photos=photos)


@app.route('/up_photo', methods=['post'])
def up_photo():
    img = request.files.get('photo')
    path = os.path.join(basedir, photo_path)
    file_path = os.path.join(path, img.filename)
    img.save(file_path)
    print('上传头像成功')
    return redirect(url_for('index_home'))


if __name__ == '__main__':
    app.run()
