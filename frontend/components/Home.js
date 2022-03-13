import React from "react"
import Link from "next/link"

import Pagination from "react-js-pagination"

import JobItem from "./job/JobItem"
import { useRouter } from "next/router"

const Home = ({ data }) => {

  const { jobs, count, resultsPerPage } = data
  const router = useRouter()
  let { page = 1, keyword } = router.query
  page = Number(page)

  let queryParams

  // If we are in the browser
  if(typeof window !== "undefined") {
    // Prepare query params
    queryParams = new URLSearchParams(window.location.search)
  }

  const handlePageClick = (currentPage) => {
    if(queryParams.has("page")) {
      queryParams.set("page", currentPage)
    } else {
      queryParams.append("page", currentPage)
    }

    router.push({
      search: queryParams.toString(),
    })
  }

  return (
    <>
      <div className="container container-fluid">
        <div className="row">
          <div className="col-xl-3 col-lg-4">
            {/* <Filters /> */}{" "}
          </div>

          <div className="col-xl-9 col-lg-8 content-left-offset">
            <div className="my-5">
              <h4 className="page-title">
              {keyword ? `${jobs.length} Results for ${keyword}` : "LATEST JOBS"}  
              </h4>
              <Link href="/stats">
                <button className="btn btn-secondary float-right stats-button">
                <i aria-hidden className="fas fa-comment"></i>  Get Topic stats
                </button>
              </Link>
              <div className="d-block">
                <Link href="/search">GO TO SEARCH</Link>
              </div>
            </div>
            {jobs && jobs.map((job) => <JobItem key={job.id} job={job} />)}

            {resultsPerPage < count && (
              <div className="d-flex justify-content-center mt-5">
                <Pagination 
                  activePage={page}
                  itemsCountPerPage={resultsPerPage}
                  totalItemsCount={count}
                  onChange={handlePageClick}
                  nextPageText={"Next"}
                  prevPageText={"Prev"}
                  firstPageText={"First"}
                  lastPageText={"Last"}
                  itemClass="page-item"
                  linkClass="page-link"
                />
              </div>
            )}

          </div>
        </div>
      </div>
    </>
  )
}

export default Home