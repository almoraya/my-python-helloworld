import json
from urllib import response
from flask import Flask

import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info("Main request successfull")
    return "Hello World!"

@app.route("/user")
def user():
    response = app.response_class(
        response=json.dumps(
            {"user":"admin"}
        )
    )
    app.logger.debug("Debugging a bug")
    app.logger.info("Warning: an user is logging in")
    return response

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps(
            {"result":"OK - healthy"}
        ),
        status=200,
        mimetype="application/json"
    )

    app.logger.info('Is this status an error?')
    return response

@app.route("/metrics")
def metrics():
    response=app.response_class(
        response=json.dumps(
            {
                "status":"success",
                "code":0,
                "data":{
                    "UserCount":140,
                    "UserCountActive":23
                }
            }
        ),
        status=200,
        mimetype="application/json"
    )
    app.logger.debug("A good place to start debugging")
    app.logger.info("A good place to start informing")
    app.logger.warning("A good place to place a warning")
    return response



if __name__ == "__main__":
    logging.basicConfig(
        filename="record.log", 
        level=logging.INFO, 
        format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'
    )
    app.run(host='0.0.0.0', port=8080)
