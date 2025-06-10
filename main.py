from flask import Flask, request, jsonify

app = Flask(__name__)
last_message = None  # global to store last received alert

@app.route('/webhook', methods=['POST'])
def webhook():
    global last_message

    try:
        json_data = request.get_json(force=True)
    except:
        json_data = None

    raw_data = request.data.decode('utf-8')

    print("\n📥 Incoming Webhook Content:")

    if json_data:
        print("✅ JSON Format Detected:")
        print(json_data)
        last_message = json_data
    else:
        print("📄 Plain Text Message:")
        print(raw_data)
        last_message = {"message": raw_data}

    return "OK", 200

@app.route('/latest_data', methods=['GET'])
def latest_data():
    if last_message:
        return jsonify(last_message)
    return jsonify({"message": "No data received yet"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
