import json
import os

# import requests


def lambda_handler(event, context):
  dynamodb_url  = os.environ.get('DYNAMODB_URL')

  payload = {
    'message': 'Hello world!',
    'dynamodb_url': dynamodb_url
  }

  return {
    "statusCode": 200,
    "body": json.dumps(payload)
  }
