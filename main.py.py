import calendar
import time
from flask import Flask
import os

app = Flask(__name__)

epoch = calendar.timegm(time.gmtime())

@app.route('/<epoch>/')
def get_epochtime(epoch):
	return str(epoch)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",6738))
    app.run(host='127.0.0.1',port=port)