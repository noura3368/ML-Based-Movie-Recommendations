import express from "express"
import cors from "cors"
import recs from "./api/recs.route.js"

const app = express()
app.use(cors()) // middle ware
app.use(express.json())

app.use("/api/v1/recs", recs)
app.use("*", (req, res) => 
res.status(404).json({error: "not found"}))

// export app as module, seperate main server code from db code
export default app
