from flask import Flask, render_template

from models import sql_models

FASTLANE_SITE = Flask(__name__)

@FASTLANE_SITE.route('/demo')
def show_demo_site():
    return render_template('demo.jinja2')

@FASTLANE_SITE.route('/process/<int:transaction_id>')
def process_payment(transaction_id):
    user = sql_models.User.get(1)
    transaction = sql_models.Transaction.get(transaction_id)
    transaction.claim_for_user(user)

    return render_template('process.jinja2')

if __name__ == '__main__':
    FASTLANE_SITE.run(port=5001)