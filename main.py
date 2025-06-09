from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    raw_data = request.data.decode('utf-8')
    print("\n📥 Raw Webhook Content:")
    print(raw_data)

    # Parse the @ format into a dictionary
    parsed_data = {}
    for line in raw_data.strip().split('\n'):
        if '@' in line:
            key, value = line.split('@', 1)
            parsed_data[key.strip()] = value.strip()

    print("\n✅ Parsed Data:")
    print(parsed_data)

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
