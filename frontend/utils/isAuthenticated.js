import axios from "axios"

export const isAuthenticatedUser = async (access_token) => {
    try {
        const response = await axios.post(`${process.env.API_URL}/api/token/verify/`, {
            token :access_token
        })

        if(response.status === 200) return true
        return false

    } catch (error) {
        return false
    }
}

/*export async function getServerSideProps({ params }) {

    try {
      const res = await axios.get(
        `${process.env.API_URL}/api/jobs/${params.id}/`
      )
  
      const job = res.data.job
      const candidates = res.data.candidates
  
      return {
        props: {
            job,
            candidates,
        },
      }
    } catch (error) {
      return {
        props: {
          error: error.response.data.detail,
        },
      }
    }
  }*/