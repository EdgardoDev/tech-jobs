/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  env: {
    API_URL: 'http://localhost:8000',
    MAPBOX_ACCESS_TOKEN: 'pk.eyJ1IjoiZWRnYXI3NCIsImEiOiJjbDBrcmdyb2IwcDQyM2R1b2c5ZzQ2MjM0In0.eHfJYLEoveqpV-X8CXBwqA'
  }
}

module.exports = nextConfig
