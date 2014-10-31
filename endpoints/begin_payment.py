__author__ = 'gsibble'

from endpoints._base_endpoint import ApiEndpoint
from flask.ext.restful import reqparse

class StartTransactionProcess(ApiEndpoint):
    location = '/process/start'

    post_parser = reqparse.RequestParser()
    post_parser.add_argument('amount', type=str)
    post_parser.add_argument('merchant_id', type=int)
    post_parser.add_argument('merchant_transaction_id', type=int)

    def post(self):
        post_args = self.post_parser.parse_args()
        merchant = self.models.Merchant.get(post_args['merchant_id'])
        new_transaction = self.models.Transaction.create(merchant=merchant,
                                                        amount=post_args['amount'],
                                                        merchant_transaction_id=post_args['merchant_transaction_id'])
        return self.make_response({'transaction_id': new_transaction.id}, 200)