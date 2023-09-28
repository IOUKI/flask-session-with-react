# flask-session-with-react

## 解決跨網域設定session問題

### 安全Cookie會話接口和SAMESITE COOKIE設定
```python
from flask.sessions import SecureCookieSessionInterface
session_cookie = SecureCookieSessionInterface.get_signing_serializer(self=SecureCookieSessionInterface, app=app)
```

```
app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = True
```