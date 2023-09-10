// initialize project with npm init 
// database code 
// env variables for your created password
import express from "express"; // calls express package 
import http from "http";
import fs from "fs";
import {spawn} from "child_process"
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import path from 'path';
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

var app = express()
app.use(express.urlencoded()); 
app.use(express.json())
//app.use(bodyParser.json());

// set the view engine to ejs
app.set('views', './views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
    //response.sendFile(__dirname + "/index.html")
    response.render(__dirname + "/index" 
    )
    //response.writeHead(200, {'Content-Type':'text/html'})
    //response.end(__dirname + "/index.html")
});
/*
app.get('/movies', function(request, response, ...availabeChoices) {
    console.log("HELLO!", request)
    response.render(__dirname + "/views/movies")
});
*/

app.post('/', (req, res) => {
    const s = spawn("python", ['model.py', req.body.movie]) 
    s.stdout.on('data', (data) => { 
        var movies = data.toString()
        res.send({'movies':movies})
        //res.send({"movies":movies, "url":"/movies"});
        //res.render("movies", {movies:movies})
        //res.redirect(__dirname + '/views/movies.ejs', {movies:movies})
    });
    //res.sendFile(__dirname + "/views/movies.ejs")
});

const port = 3000
app.listen(port)
console.log(`Listening at http://localhost:${port}`)
