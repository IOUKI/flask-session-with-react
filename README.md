# flask-session-with-react

## 解決跨網域設定session問題

### 安全Cookie會話接口
```python
from flask.sessions import SecureCookieSessionInterface
session_cookie = SecureCookieSessionInterface.get_signing_serializer(self=SecureCookieSessionInterface, app=app)
```

### 確保在建立請求後將相同的會話添加到響應中，而不是在每個路由上調用它，這邊我們使用after_request裝飾器來完成
```python
@app.after_request
def cookies(response):
    same_cookie = session_cookie.dumps(dict(session))
    response.headers.add("Set-Cookie", f"my_cookie={same_cookie}; Secure; HttpOnly; SameSite=None; Path=/;")
    return response
```