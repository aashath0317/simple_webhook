from flask import Flask, request
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook:", data)
    # Save the signal to a file or send it to MT4
    with open("/tmp/mt4_signal.txt", "w") as f:
        f.write(str(data))
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
