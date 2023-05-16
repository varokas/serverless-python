from fastapi import FastAPI
from mangum import Mangum
import boto3
from botocore.config import Config
import json

from params_aws import params_aws
from params_aws import model

REGION="ap-southeast-1"

app = FastAPI(title="python-serverless")

@app.get("/hello")
def hello():
    return {"hello": "world"}

@app.get("/params_raw")
def params_raw():
    client = boto3.client('ssm', config=Config(region_name=REGION))
    response = client.get_parameters(Names=["test"])
    params = response["Parameters"]

    return {p["Name"]:json.loads(p["Value"]) for p in params}

@app.get("/params")
def params():
    return params_aws.get_parameter(name='test', modelType=model.DBConfig)

handler = Mangum(app)
