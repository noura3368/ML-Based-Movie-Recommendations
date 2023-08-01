// initialize project with npm init 
// database code 
// env variables for your created password
//import app from "./server.js"
//import mongodb from "mongodb"
//import recsDAO from "./dao/recsDAO.js" // common pattern to write objects that works with db

import express from "express"; // calls express package 
import http from "http";
import fs from "fs";
import { dirname } from 'path';
import { fileURLToPath } from 'url';
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

var app = express()
app.use(express.json())

app.get('/', function(request, response) {
    console.log('GET /')
    response.sendFile(__dirname + "/index.html")
    //response.writeHead(200, {'Content-Type':'text/html'})
    //response.end(__dirname + "/index.html")
});
app.get('/movies', function(request, response) {
    console.log('GET /')
    response.sendFile(__dirname + "/movies.html")
});
app.post('/movies', (req, res) => {
    console.log("noura!")
    console.log(req["body"]["val"])
    res.sendFile(__dirname + "/movies.html")
});

const port = 3000
app.listen(port)
console.log(`Listening at http://localhost:${port}`)
