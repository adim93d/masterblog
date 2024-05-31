from flask import Flask, render_template
import json
app = Flask(__name__)


def read_json(json_file):
    with open(json_file, 'r') as fileobj:
        data = json.load(fileobj)
    return data


@app.route('/')
def index():
    blog_posts = read_json('/home/sec/PycharmProjects/masterblog/masterblog/blog_posts.json')
    return render_template('index2.html', posts=blog_posts)


if __name__ == '__main__':
    app.run()
