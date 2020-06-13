const socket = io();

const app = new Vue({
  el: "#app",
  data: {
    usuario: "",
    mensaje: "",
    mensajes: [],
  },
  methods: {
    enviar() {
      if (!this.usuario) {
        alert("Falta llenar el usuario.");
        return;
      }
      if (!this.mensaje) {
        alert("Falta llenar el mensaje.");
        return;
      }
      const objeto = {
        usuario: this.usuario,
        mensaje: this.mensaje,
      };
      socket.emit("mensaje", objeto);
      this.mensajes.push(objeto);
      this.mensaje = "";
    },
  },
  created() {
    socket.on("inicial", (mensajes) => {
      this.mensajes = mensajes;
    });
    socket.on("mensaje", (objeto) => {
      this.mensajes.push(objeto);
    });
  },
});
