from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Try to parse JSON
    try:
        json_data = request.get_json(force=True)
    except:
        json_data = None

    # If not JSON, read raw data as plain text
    raw_data = request.data.decode('utf-8')

    print("\n📥 Incoming Webhook Content:")

    if json_data:
        print("✅ JSON Format Detected:")
        print(json_data)
    else:
        print("📄 Plain Text Message:")
        print(raw_data)

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
