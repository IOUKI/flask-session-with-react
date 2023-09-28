from flask import Flask, request, render_template, session, redirect, jsonify
from flask.sessions import SecureCookieSessionInterface
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
app.secret_key = "#@*(!#fdsfjkl;j)"

app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"

# Session Cookie 設定
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True

# 處理 samesite=None 的問題
session_cookie = SecureCookieSessionInterface.get_signing_serializer(self=SecureCookieSessionInterface, app=app)
CORS(
    app=app,
    supports_credentials=True,
)
Session(app)

# 設定session cookie
# @app.after_request
# def cookies(response):
#     sameCookie = session_cookie.dumps(dict(session))
#     response.headers.add("Set-Cookie", f"my_cookie={sameCookie}; Secure; HttpOnly; SameSite=None; Path=/;")
#     return response

# 取得session內的數值
@app.route('/')
def index():
    if not session.get('username'):
        return jsonify({'alert': 'session not found.'}), 404

    print(session['username'])
    response = jsonify({'username': session['username']})
    return response, 200

# 登入
@app.route('/login', methods=['POST'])
def login():
    try: 
        username = request.get_json()['username']
        print('login username: ', username)
        session['username'] = username
        return jsonify({"username": session['username']}), 201
    except Exception as e:
        print(e)
        return '', 404

# 登出
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)