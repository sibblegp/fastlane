__author__ = 'gsibble'

from endpoints._base_endpoint import ApiEndpoint
from flask.ext.restful import reqparse

class PushTransaction(ApiEndpoint):
    location = '/process/push'

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('url', type=str)

    def post(self):
        post_args = self.post_parser.parse_args()

        transaction_id = int(post_args['url'].split('process/')[1])

        transaction = self.models.Transaction.get(transaction_id)

        return {'user_name': transaction.user.first_name}
