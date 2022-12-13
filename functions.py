import json
POST_PATH = "posts.json"


def load_posts_from_json(path):
    with open(path, mode="r", encoding="utf-8") as filename:
        return json.load(filename)


def get_posts_by_word(word):
    posts = load_posts_from_json(POST_PATH)
    result = []
    for item in posts:
        if word.lower() in item["content"].lower():
            result.append(item)
    return result


def post_upload(content, pic_path):
    posts = load_posts_from_json(POST_PATH)
    data = {"pic": pic_path, "content": content}
    posts.append(data)
    try:
        with open(POST_PATH, 'w', encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
    except Exception as e:
        return e

