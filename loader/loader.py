from pathlib import Path

from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import write_posts_to_json
import logging
import os

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('loader')
logger.addHandler(logging.StreamHandler())

loader_bp = Blueprint('loader_bp', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'png'}

@loader_bp.route('/post', methods=['GET'])
def post():
    return render_template('post_form.html')


@loader_bp.route('/post_uploaded', methods=['POST'])
def post_post():
    picture = request.files.get('picture')
    filename = picture.filename
    text = request.form.get('content')
    write_posts_to_json(filename, text)
    url_file = f'http://127.0.0.1:5000/uploads/images/{filename}'
    if filename.split('.')[-1] not in ALLOWED_EXTENSIONS:
        logger.info('Ext no allowed')
        return f'ERR: Your file type not supported: {filename.split(".")[-1]}'
    else:
        picture.save(f'C:\\PY\\PROJECTS\\HomeWork12.3-final\\uploads\\images\\{filename}')
        if os.path.exists(f'C:\\PY\\PROJECTS\\HomeWork12.3-final\\uploads\\images\\{filename}'):
            return render_template('post_uploaded.html', url_file=url_file, text=text)
        else:
            logger.error('Errors')
            return f'Error loading {filename}'

