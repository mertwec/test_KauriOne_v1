import json
from flask import Flask, jsonify


app = Flask(__name__)
app.config.update(SERVER_NAME="localhost:5050",
                  DEBUG=False,
                  )


@app.route('/api_local')
def index():
    return jsonify({'name': 'Valentin',
                    'email': 'val.work@example.com',
                    'age': 30,
                    'married': True,
                    'skils': ['Python3', 'Flask', 'json'],
                    'some': None, 
                    })


if __name__ == "__main__":
    app.run()
