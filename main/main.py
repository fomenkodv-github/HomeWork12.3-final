from flask import Flask, request, render_template, Blueprint, send_from_directory

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def main():
    return render_template('index.html')


@main_bp.route('/index.html')
def main2():
    return render_template('index.html')
