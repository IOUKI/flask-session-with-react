import { useState } from "react"
import { BASE_URL } from "../api/apiUrl"

const Login = () => {

  const [name, setName] = useState("")

  // 送出表單
  const submitHandle = async () => {

    if (name == "") {
      alert('請輸入名稱')
      return
    }

    fetch(`${BASE_URL}/login`, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json"
      },
      credentials: 'include',
      body: JSON.stringify({ username: name }),
    })
      .then(response => {
        if (response.status === 201) {
          console.log('logged in!')
        }
      })
      .catch(error => console.log(error))
  }

  // 確認有無登入
  const loginCheckHandle = () => {
    fetch(`${BASE_URL}`, {
      method: 'GET',
      headers: {
        "Content-Type": "application/json"
      },
      credentials: 'include', // 這是重要的部分，表示要發送Cookie
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => {
        console.error('錯誤:', error);
      });
  }

  // 登出按鈕
  const logoutCheckHandle = () => {
    fetch(`${BASE_URL}/logout`, {
      method: 'GET',
      credentials: 'include',
    })
      .then(response => {
        console.log(response.status)
        document.cookie.split(";").forEach(function (cookie) {
          var eqPos = cookie.indexOf("=");
          var name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
          document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
        });
      })
      .catch(error => console.log(error))
  }

  return (
    <>
      <form>
        <input
          type="text"
          placeholder="Name"
          onChange={(e) => {
            setName(e.target.value)
          }}
        />
        <button
          type="button"
          onClick={submitHandle}
        >
          Register
        </button>
      </form>

      <br />
      
      <button
        onClick={loginCheckHandle}
      >
        Logged In Check
      </button>
      
      <br />
      <br />
      
      <button type="button"
        onClick={logoutCheckHandle}
      >logout</button>
    </>
  )
}

export default Login