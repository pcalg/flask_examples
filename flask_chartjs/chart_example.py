"""
Small flask example showing how to use an api with Chart.js.

In this case the api is provided in this project by the get_data method.

pca - 2019

"""

from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)

data = [{'tenor': 1.0, 'value': 0.05}, {'tenor': 1.1, 'value': 0.052}, {'tenor': 2.0, 'value': 0.07},
        {'tenor': 3.0, 'value': 0.0712}, {'tenor': 3.5, 'value': 0.075}, {'tenor': 5.0, 'value': 0.089}]


@app.route('/', methods=['GET'])
def home():
    return render_template('graph_data.html')


@app.route('/api/v1/resources/data/all')
def get_data():
    return jsonify(data)


if __name__ == '__main__':
    app.run()
