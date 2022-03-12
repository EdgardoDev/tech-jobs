import React from "react"
import Link from "next/link"
import JobItem from "./job/JobItem"
import { useRouter } from "next/router";

const Home = ({ data }) => {

  const { jobs, count, resPerPage } = data
  const router = useRouter()
  let { keyword } = router.query

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
          </div>
        </div>
      </div>
    </>
  );
};

export default Home