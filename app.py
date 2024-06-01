from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)


BLOG_DATA = 'blog_posts.json'


def read_json(json_file):
    with open(json_file, 'r') as fileobj:
        data = json.load(fileobj)
    return data


def write_json(json_file, data):
    with open(json_file,'w') as fileobj:
        json.dump(data, fileobj, indent=4)


def add_data_to_json(json_file, new_data):
    data = read_json(json_file)
    data.append(new_data)
    write_json(json_file, data)


def last_id(json_file):
    last_item = -1
    data = read_json(json_file)
    last_id_num = data[last_item]['id']
    return last_id_num

def fetch_post_by_id(post_id, data):
    for post in data:
        if post['id'] == post_id:
            return post
    return None


@app.route('/')
def index():
    blog_posts = read_json(BLOG_DATA)
    return render_template('index2.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':

        post_id = int(last_id(BLOG_DATA)) + 1
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        new_post = {"id": post_id,
                    "author": author,
                    "title": title,
                    "content": content
                    }

        add_data_to_json(BLOG_DATA, new_post)
        return redirect(url_for('index'))
    return render_template('/add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    data = read_json(BLOG_DATA)
    updated_data = []
    for post in data:
        if post['id'] != post_id:
            updated_data.append(post)
    write_json(BLOG_DATA, updated_data)
    return redirect(url_for('index'))


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    data = read_json(BLOG_DATA)
    post = fetch_post_by_id(post_id, data)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post details
        post['title'] = request.form['title']
        post['author'] = request.form['author']
        post['content'] = request.form['content']

        # Write the updated data back to the JSON file
        write_json(BLOG_DATA, data)
        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
