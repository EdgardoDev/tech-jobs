import React, { useState } from "react"
import Image from "next/image"
import { useRouter } from "next/router"

const Search = () => {

    const [keyword, setKeyword] = useState("")
    const [location, setLocation] = useState("")
    const router = useRouter()

    const submitHandler = async (e) => {
        e.preventDefault()
        
        if(keyword) {
            let searchQuery = `/?keyword=${keyword}`
            if(location) searchQuery = searchQuery.concat(`&location=${location}`)
            router.push(searchQuery)
        } else {
            router.push("/")
        }
    }

  return (
    <div className="modal-mask">
      <div className="modal-wrapper">
        <div className="left">
          <div style={{ width: "100%", height: "100%", position: "relative" }}>
            <Image src="/images/job-search.svg" alt="search" layout="fill"/>
          </div>
        </div>
        <div className="right">
          <div className="right-content-wrapper">
            <div className="header-wrapper">
              <h2> SEARCH</h2>
            </div>
            <form className="form" onSubmit={submitHandler}>
              <div className="input-wrapper">
                <div className="input-box">
                  <i aria-hidden className="fas fa-search"></i>
                  <input
                    type="text"
                    placeholder="Enter Your Keyword"
                    value={keyword}
                    onChange={(e) => setKeyword(e.target.value)}
                    required
                  />
                </div>
                <div className="input-box">
                  <i aria-hidden className="fas fa-industry"></i>
                  <input
                    type="text"
                    placeholder="Enter City And State"
                    value={location}
                    onChange={(e) => setLocation(e.target.value)}
                  />
                </div>
              </div>
              <div className="search-button-wrapper">
                <button type="submit" className="search-button">
                <i aria-hidden className="fas fa-search"></i> SEARCH
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Search