from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Handle authorization code
    authorization_code = request.args.get('code')
    # Process the authorization code

    return "Authorization successful. You can close this window."

if __name__ == '__main__':
    app.run(port=8888)




