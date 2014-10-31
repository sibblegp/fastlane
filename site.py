from flask import Flask, render_template

from models import sql_models

FASTLANE_SITE = Flask(__name__)

@FASTLANE_SITE.route('/demo')
def show_demo_site():
    return render_template('demo.jinja2')

@FASTLANE_SITE.route('/process/<transaction_id>')
def process_payment():
    return render_template('process.jinja2')

if __name__ == '__main__':
    FASTLANE_SITE.run(port=5001)