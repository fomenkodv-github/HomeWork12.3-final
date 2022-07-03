from flask import Flask, request, render_template, Blueprint, send_from_directory
from functions import search_by_word

search_bp = Blueprint('search_bp', __name__)


@search_bp.route('/search')
def search():
    strg = request.args['s']
    posts = search_by_word(strg)
    return render_template('post_list.html', posts=posts, strg=strg)
