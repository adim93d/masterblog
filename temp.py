
import json


def read_json(json_file):
    with open(json_file, 'r') as fileobj:
        data = json.load(fileobj)
    return data


blog_posts = read_json('/home/sec/PycharmProjects/masterblog/masterblog/blog_posts.json')
for post in blog_posts:
    for key, value in post.items():
        print(key, value)

