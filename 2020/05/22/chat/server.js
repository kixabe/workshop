const http = require("http");
const path = require("path");
const express = require("express");
const SocketIO = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = SocketIO(server);

// 1. cola de mensajes por sala (una sola sala)
// 2. manejar los hilos de conexión (ingresan)
// 3. enviar todos los mensajes ni bien se conecta

// síncrona
// resultado = conn.query('SELECT * FROM productos')
// linea 5, espera hasta que retorne

// asíncrona
// function callback(registros) { // podemos trabajar con registros }
// conn.query('SELECT * FROM productos', callback)
// linea 5, se ejecuta directamente

// exponer "public" al servidor "/"
app.use(express.static(path.join(__dirname, "public")));

const mensajes = [];

io.on("connection", (socket) => {
  socket.emit("inicial", mensajes);
  socket.on("mensaje", (mensaje) => {
    mensajes.push(mensaje);
    socket.broadcast.emit("mensaje", mensaje);
  });
});

server.listen(1234, () => {
  console.log("Servidor de chat iniciado");
});

// http://localhost:1234
