from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    json_content = request.get_json(silent=True)
    print(json_content)
    return "Received!"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9874)
