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
app.use(express.json());
const PORT = process.env.PORT || 3030;


// set the view engine to ejs
app.set('views', './views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
    response.render(__dirname + "/index" )

});


app.post('/', (req, res) => {
    console.log(process.env.API)
    const s = spawn("python3", ['./model.py', req.body.movie, process.env.API]) 
    s.stdout.on('data', (data) => { 
        var movies = data.toString()
        console.log(movies)
        res.send({'movies':movies})
    });
    s.stderr.on('data', (data) => {
        console.log("hello!")
    })
});

app.listen(PORT, () => {
    console.log(`server started on port ${PORT}`);
  });
