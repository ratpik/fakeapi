from flask import Flask, Response
from models import Person
import json

app = Flask(__name__)

@app.route("/persons")
def hello():
    p = [Person().__dict__ for i in range(10)]
    return Response(json.dumps(p), mimetype='application/json')

if __name__ == "__main__":
    app.run()
