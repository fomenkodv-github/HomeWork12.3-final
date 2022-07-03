import logging
import os

from flask import Flask, send_from_directory

from loader.loader import loader_bp
from main.main import main_bp
from search.search import search_bp

logging.basicConfig(level=logging.DEBUG)




POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"
TEMPLATES = 'templates'

app = Flask(__name__, template_folder=TEMPLATES)

UPLOAD_FOLDER = os.path.join(app.instance_path, 'uploads\\images')

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1 MB upload limit
app.config['JSON_AS_ASCII'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(main_bp)
app.register_blueprint(loader_bp)
app.register_blueprint(search_bp)


# @app.route("/list")
# def page_tag():
#    pass


# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#    pass


# @app.route("/post", methods=["POST"])
# def page_post_upload():
#    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

print(app.instance_path)
