// initialize project with npm init 
// database code 
// env variables for your created password
import app from "./server.js"
import mongodb from "mongodb"
//import recsDAO from "./dao/recsDAO.js" // common pattern to write objects that works with db

const MongoClient = mongodb.MongoClient
const mongo_username = ""
const mongo_password = ""
// `` allows us to use js vars inside of string
const uri = `mongodb+srv://${mongo_username}:${mongo_password}@cluster0.u4xzqb4.mongodb.net/?retryWrites=true&w=majority`
const port = 8000

MongoClient.connect(
    uri,
    {
        "maxPoolSize":50,
        "wtimeoutMS":2500,
        "useNewUrlParser": true
    } // js opject
).catch(err => {
    // => creates a function without name, err is parameter
    console.error(err.stack)
    process.exit(1)
})
.then( // first connect then do smth (async function)
    async client =>{
        app.listen(port, () => {
            console.log(`listening on port ${port}`)
        }) // start server
    } // coming from connection from db
)