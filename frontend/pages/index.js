import Layout from '../components/layout/Layout'
import Home from '../components/Home'

import axios from 'axios'

export default function Index({ data }) {
  console.log("jobs", data);
  return (
    <Layout>
      <Home data={data} />
    </Layout>
  )
}

export async function getServerSideProps({ query }) {

  const keyword = query.keyword || ""
  const location = query.location || ""
  const page = query.page || ""

  const queryString = `keyword=${keyword}&location=${location}&page=${page}`

  const res = await axios.get(`${process.env.API_URL}/api/jobs?${queryString}`)
  const data = res.data

  return {
    props: {
      data,
    },
  }
}
