import React, { useContext } from "react"
import Link from "next/link"
import Image from "next/image"
import AuthContext from "../../context/AuthContext"

const Header = () => {

  // Get logged in user from the state
  const { loading, user } = useContext(AuthContext)

  return (
    <div className="nav-wrapper">
      <div className="nav-container">
        <Link href="/">
          <div className="logo-wrapper">
            <div className="logo-image-wrapper">
              <Image width="40" height="40" src="/images/job-search.png" alt="" />
            </div>
            <span className="logo-one">TECH</span>
            <span className="logo-two">JOBS</span>
          </div>
        </Link>
        <div className="buttons-wrapper">
          <Link href="/employeer/jobs/new">
            <button className="post-a-job-button">
              <span><i aria-hidden className="fas fa-briefcase"></i> POST JOB</span>
            </button>
          </Link>
          {user ? (
            <div className="btn dropdown ml-3">
              <a
                className="btn dropdown-toggle mr-4"
                id="dropdownMenuButton"
                data-toggle="dropdown"
                aria-hashpopup="true"
                aria-expanded="false"
              >
                <span>Hello, {user.first_name}</span>
              </a>
              <div className="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <Link href="/employer/jobs">
                  <a className="dropdown-item">
                    My Jobs
                  </a>
                </Link>
                <Link href="/current-user/applied">
                  <a className="dropdown-item">
                    Jobs Applied
                  </a>
                </Link>
                <Link href="/current-user">
                  <a className="dropdown-item">
                    Profile
                  </a>
                </Link>
                <Link href="/upload/resume">
                  <a className="dropdown-item">
                    Upload Resume
                  </a>
                </Link>
                <Link href="/">
                  <a className="dropdown-item text-danger">
                    Logout
                  </a>
                </Link>
              </div>
            </div>
          ) : (
            !loading && (
            <Link href="/login">
              <button className="login-button-header">
                <span><i aria-hidden className="fas fa-arrow-right"></i> LOGIN</span>
              </button>
            </Link>
            )
          )}
          
        </div>
      </div>
    </div>
  );
};

export default Header;