import json
import re

url = 'http://127.0.0.1:5000/uploads/images/'
file = 'C:\\PY\\PROJECTS\\HomeWork12.3-final\\posts.json'


def read_posts_from_json():
    with open(file, 'r', encoding='UTF-8') as f:
        posts_json = json.load(f)
    return posts_json


def write_posts_to_json(filename, content):
    new_post = {"pic": url+filename, "content": content}
    posts_json = read_posts_from_json()
    posts_json.insert(0, new_post)
    with open(file, 'w+', encoding="UTF-8") as f:
        json.dump(posts_json, f, ensure_ascii=False)
    return f"Written, {posts_json[0].get('pic')}"


regex = r'#(\w+)'  # Search a word with attached hashtag #


def search_by_word(s):
    hashtags = []
    for post in read_posts_from_json():
        if s.lower() in re.findall(regex, post.get('content')):  # Match a searchword in hashtangs by regex
            hashtags.append(post)
    return hashtags  # return a list of dicts of matched hashtags
