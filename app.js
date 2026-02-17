const http = require('http');

const server = http.createServer((req, res) => {
  res.end("Hello from DEV branch - Node.js Docker App");
});

server.listen(3000, () => {
  console.log("Node app running on port 3000");
});
