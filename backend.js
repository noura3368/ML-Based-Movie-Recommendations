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

const host = 'localhost';
const port = 3000;
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const requestListener = function (req, res) {
    fs.promises.readFile(__dirname + "/index.html")
        .then(contents => {
            res.setHeader("Content-Type", "text/html");
            res.writeHead(200);
            console.log('fdfsd')
            res.end(contents);
        })
        .catch(err => {
            console.log('dss')
            res.writeHead(500);
            res.end(err);
            return;
        });
};
const server = http.createServer(requestListener);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});

var app = express(); // creates application to work with

app.listen(3000); // listen on port 3000
app.use(express.json());

app.get("/", (req, res)=> { //route of the url we want to get, res is response from server
    res.sendFile(__dirname + "/index.html");
});

app.post("/movies", (req, res)=>{
    console.log(req.body);
});
