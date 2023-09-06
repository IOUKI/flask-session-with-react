from flask import Flask, request, render_template, session, redirect, jsonify
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.secret_key = "#@*(!#fdsfjkl;j)"
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
CORS(
    app=app,
    supports_credentials=True
)
Session(app)

@app.route('/')
def index():
    if not session.get('username'):
        return jsonify({'alert': 'session not found.'}), 404

    print(session['username'])
    response = jsonify({'username': session['username']})
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response, 200

@app.route('/login', methods=['POST'])
def login():
    try: 
        username = request.get_json()['username']
        print('Received username: ', username)
        session['username'] = username
        return jsonify({"username": session['username']}), 201
    except Exception as e:
        print(e)
        return '', 404

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)