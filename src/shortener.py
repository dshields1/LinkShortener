import boto3

def shorten_url(event, context):
    return {
        "statusCode": 200,
        "headers": {},
        "body": 'Hello world!'
    }

def ui(event, context):
    return {
        "statusCode": 200,
        "headers": {},
        "body": 'Hello world!'
    }

def inspect(event, context):
    return {
        "statusCode": 200,
        "headers": {},
        "body": 'Hello world!'
    }

def redirect(event, context):
    return {
        "statusCode": 200,
        "headers": {},
        "body": 'Hello world!'
    }