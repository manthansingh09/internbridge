const express = require('express')
const cors = require('cors')
const jwt = require('jsonwebtoken')
const axios = require('axios')
const bodyParser = require('body-parser')


const app = express()
app.use(cors())
app.use(bodyParser.json())


const PORT = process.env.API_PORT || 4000


// Simple public internships proxy (fetching AICTE/public data or seeded DB)
app.get('/api/internships/public', async (req, res) => {
try {
// Example: call AICTE public endpoint if configured, else fallback to DB
const aicteEndpoint = process.env.NEXT_PUBLIC_AICTE_ENDPOINT || process.env.AICTE_API_ENDPOINT
if (aicteEndpoint) {
const r = await axios.get(aicteEndpoint)
return res.json(r.data)
}
return res.json([])
} catch (err) {
console.error(err)
return res.status(500).json({ error: 'failed' })
}
})


app.listen(PORT, () => console.log(`API gateway started on ${PORT}`))