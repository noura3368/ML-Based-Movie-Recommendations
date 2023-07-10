// initialize project with npm init 
// database code 
// env variables for your created password
//import app from "./server.js"
//import mongodb from "mongodb"
//import recsDAO from "./dao/recsDAO.js" // common pattern to write objects that works with db

import express from "express"; // calls express package 
var app = express(); // creates application to work with

app.listen(3000); // listen on port 3000
app.use(express.json());
app.get("/", (req, res)=> { //route of the url we want to get, res is response from server
    res.sendFile("index.html", {root: "C:/Users/noura/Documents/ML-Based-Movie-Recommendations/"});
})
app.post("/movies", (req, res) => {
    console.log(req.body);
});
/*
const MongoClient = mongodb.MongoClient
const mongo_username = ""
const mongo_password = ""
// `` asllows us to use js vars inside of string
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
        await rmecsDAO.injectDB(Client) // sending db connection for recsDAO
        app.listen(port, () => { //runs recs.route.js 
            console.log(`listening on port ${port}`)
        }) // start server
    } // coming from connection from db
)
*/