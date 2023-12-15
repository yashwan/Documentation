// const http = require('http');

// const server = http.createServer(
//     (req, res)=>{
//         console.log(req)
//         console.log("server started");
//         console.log(new Date().toLocaleDateString());
//         console.log('------------------------------------------------------------------------------------------------')
//         res.writeHead(200, {
//             "Content-Type": "application/json"
//         })
//         res.end("response received")
//     }
// )
// const port = 4000
// server.listen(port, ()=> {
//     console.log(`server listening on port ${port}`)
// });




const express = require("express");

const app = express();
// app.use(express.json());

const port = 4000
app.get(`/user/`, (req, res)=> {
    res.end()
})

app.get(`/user/:uuid`, (req, res)=> {
    res.end()
})


app.get(`/user/search`, (req, res)=> {
    res.end()
})

app.listen(port, ()=>{
    console.log(`listening on ${port}`)
})