import React from "react"
import Link from "next/link"
import Image from "next/image"

const Header = () => {
  return (
    <div className="nav-wrapper">
      <div className="nav-container">
        <Link href="/">
          <div className="logo-wrapper">
            <div className="logo-image-wrapper">
              <Image width="40" height="40" src="/images/logo.png" alt="" />
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

          <Link href="/login">
            <button className="login-button-header">
              <span><i aria-hidden className="fas fa-arrow-right"></i> LOGIN</span>
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Header;