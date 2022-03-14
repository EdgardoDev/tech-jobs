import React, { useState, useContext, useEffect } from "react"
import { useRouter  } from "next/router"
import Image from "next/image"

import AuthContext from "../../context/AuthContext"

const Login = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const router = useRouter()

    const { loading, error, isAuthenticated, login } = useContext(AuthContext)

    useEffect(() => {
        if (error) {
           console.log(error); 
        }

        if (isAuthenticated && !loading) {
            router.push("/")
        }
    }, [isAuthenticated, error, loading])

    const submitHandler = (e) => {
        e.preventDefault()
        login({ username: email, password })
    }

  return (
    <div className="modal-mask">
      <div className="modal-wrapper">
        <div className="left">
          <div style={{ width: "80%", height: "80%", position: "relative" }}>
            <Image src="/images/login.svg" alt="login" layout="fill" />
          </div>
        </div>
        <div className="right">
          <div className="right-content-wrapper">
            <div className="header-wrapper">
              <h2> LOGIN</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="input-wrapper">
                <div className="input-box">
                  <i aria-hidden className="fas fa-envelope"></i>
                  <input 
                    type="email" 
                    placeholder="Enter Your Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    pattern="\S+@\S+\.\S+"
                    title="Invalid Email"
                    required 
                  />
                </div>
                <div className="input-box">
                  <i aria-hidden className="fas fa-key"></i>
                  <input
                    type="password"
                    placeholder="Enter Your Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
              </div>
              <div className="login-button-wrapper">
                <button type="submit" className="login-button"> 
                {loading ? (
                    <>
                        <i aria-hidden className="fas fa-hourglass-start"></i> AUTHENTICATING...
                    </>
                ) : (
                    <>
                        <i aria-hidden className="fas fa-arrow-right"></i> LOGIN
                    </>
                )}
                </button>
              </div>
              <p style={{ textDecoration: "none" }} className="signup">
                New to Tech Jobs? <a href="/register">Create an account</a>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Login