
import flask
import os
import logging

FINAL_DATE = os.environ.get('FINAL_DATE')

logging.basicConfig(level=logging.INFO)

app = flask.Flask(__name__)

@app.route('/')
def index():
    logging.info(FINAL_DATE)
    return flask.render_template('index.html', final_date=FINAL_DATE)

if __name__ == '__main__':
    app.run(debug=True)