import React from "react"
import Link from "next/link"
import Layout from "./Layout";

const NotFound = () => {
  return (
    <Layout title="Page Not Found">
        <div className="page-not-found-wrapper">
            <img 
                src="/images/404.svg" 
                height="344" 
                width="636" 
                alt="404_not_found" 
            />

            <h5 className="mt-5">
                Page Not Found. Back to <Link href="/">HOMEPAGE</Link>{" "}
            </h5>
        </div>
    </Layout>
  )
}

export default NotFound