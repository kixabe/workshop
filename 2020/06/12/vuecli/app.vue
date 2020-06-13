<template>
  <div>
    <label>
      <input type="checkbox" v-model="autoplay" />
      AutoPlay
    </label>

    <br /><br />

    <div v-if="fuente">
      <video
        @ended="alTerminar"
        v-if="fuente"
        controls
        :src="fuente"
        :autoplay="autoplay"
      ></video>
      <p>Video {{ indice + 1 }}</p>
    </div>
    <div v-else>
      No hay más videos.
    </div>
  </div>
</template>

<script>
export default {
  data: () => ({
    autoplay: true,
    indice: -1,
    fuente: "",
    fuentes: [
      "http://video1", // ...
    ],
  }),
  created() {
    this.reproducir();
  },
  methods: {
    reproducir() {
      if (this.autoplay) {
        if (++this.indice < this.fuentes.length) {
          this.fuente = this.fuentes[this.indice];
        } else {
          this.fuente = "";
          this.indice = -1;
        }
      }
    },
    alTerminar() {
      this.reproducir();
    },
  },
  watch: {
    autoplay(valor) {
      if (valor) this.reproducir();
    },
  },
};
</script>
