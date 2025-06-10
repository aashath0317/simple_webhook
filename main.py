from flask import Flask, request, jsonify

app = Flask(__name__)

# To store the latest parsed signal
latest_signal = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    raw_data = request.data.decode('utf-8').strip()

    print("\n📥 Incoming Webhook Content:")
    print("📄 Plain Text Message:")
    print(raw_data)

    # Parse key:value pairs like "entry:buy,price:4321.55"
    parsed_data = {}
    for item in raw_data.split(','):
        if ':' in item:
            key, value = item.split(':', 1)
            parsed_data[key.strip()] = value.strip()

    # Save latest signal
    global latest_signal
    latest_signal = parsed_data

    print("\n✅ Parsed Data:")
    print(parsed_data)

    return "OK", 200


@app.route('/latest_data', methods=['GET'])
def get_latest_data():
    return jsonify(latest_signal)


if __name__ == '__main__':
    # Use port 5000 to avoid conflicts with system services on port 80
    app.run(host='0.0.0.0', port=5000)
