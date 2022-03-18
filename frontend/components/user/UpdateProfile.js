import React, { useState, useContext, useEffect } from "react"
import { useRouter  } from "next/router"
import Image from "next/image"

import AuthContext from "../../context/AuthContext"
import { toast } from "react-toastify"

const UpdateProfile = () => {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const router = useRouter()

    const { loading, error, user, clearErrors } = useContext(AuthContext)

    useEffect(() => {
        if(user) {
            setFirstName(user.first_name)
            setLastName(user.last_name)
            setEmail(user.email)
        }

        if (error) {
            toast.error(error); 
            clearErrors()
        }

    }, [error, user, loading])

    const submitHandler = (e) => {
        e.preventDefault()
        //register({ firstName, lastName, email, password })
    }

    return (
    <div className="modal-mask">
      <div className="modal-wrapper">
        <div className="left">
          <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <Image src="/images/profile.svg" alt="register" layout="fill" />
          </div>
        </div>
        <div className="right">
          <div className="right-content-wrapper">
            <div className="header-wrapper">
              <h2> PROFILE</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="input-wrapper">
                <div className="input-box">
                  <i aria-hidden className="fas fa-user"></i>
                  <input 
                    type="text" 
                    placeholder="Enter First Name" 
                    value={firstName} 
                    onChange={(e) => setFirstName(e.target.value)} 
                    required 
                    />
                </div>

                <div className="input-box">
                  <i aria-hidden className="fas fa-user-tie"></i>
                  <input 
                    type="text" 
                    placeholder="Enter Last name" 
                    required
                    value={lastName} 
                    onChange={(e) => setLastName(e.target.value)}
                    />
                </div>

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
                    minLength={6}
                    required
                  />
                </div>
              </div>
              <div className="register-button-wrapper">
                <button type="submit" className="register-button">
                {loading ? (
                    <>
                        <i aria-hidden className="fas fa-spinner"></i> UPDATING...
                    </>
                ) : (
                    <>
                        <i aria-hidden className="fas fa-address-card"></i> UPDATE
                    </>
                )}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  )
}

export default UpdateProfile