from flask import Flask, request, jsonify

app = Flask(__name__)

latest_parsed_data = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_parsed_data
    raw_data = request.data.decode('utf-8')
    parsed_data = {}
    for line in raw_data.strip().split('\n'):
        if '@' in line:
            key, value = line.split('@', 1)
            parsed_data[key.strip()] = value.strip()

    latest_parsed_data = parsed_data

    return "OK", 200

@app.route('/latest_data', methods=['GET'])
def latest_data():
    return jsonify(latest_parsed_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
