import json

import numpy as np

def hello(event, context):
    a = np.arange(15)

    response = {
        "statusCode": 200,
        "body": json.dumps({ "sum": int(np.sum(a)) })
    }

    return response
