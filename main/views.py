from flask import Blueprint, render_template, request
from functions import load_posts_from_json, get_posts_by_word
import logging

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
logging.basicConfig(filename='basic.log', level=logging.INFO)

@main_blueprint.route("/")
def page_index():
    return render_template('index.html')


@main_blueprint.route("/search/")
def page_tag():
    word = request.args.get("word")
    logging.info(f'Поиск: {word}')
    posts_list = get_posts_by_word(word)
    return render_template('post_list.html', posts_list=posts_list, word=word)
