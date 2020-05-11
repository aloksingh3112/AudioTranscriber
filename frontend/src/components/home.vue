<template>
  <div>
    <h2>Audio Data</h2>
    <hr />
    <div v-if="audioData.length>0">
      <template v-for="item in audioData">
        <Transcribe v-bind:key="item.id" v-bind:item="item" @changeData="changeData($event)"></Transcribe>
      </template>
    </div>
    <div v-else>No Audio found 😭😭</div>
  </div>
</template>
<script>
import axios from "axios";
import { GET_AUDIO } from "../config/url";
import Transcribe from "./transcribe";
export default {
  name: "Home",
  data() {
    return {
      audioData: []
    };
  },
  mounted() {
    this.getAudio();
  },

  methods: {
    getAudio() {
      const OPTIONS = {
        headers: {
          Authorization: localStorage.getItem("token")
            ? "JWT" + " " + localStorage.getItem("token")
            : ""
        }
      };
      console.log("hello", OPTIONS);

      axios
        .get(GET_AUDIO, OPTIONS)
        .then(responseData => {
          console.log(responseData);
          this.audioData = [...responseData.data.data];
        })
        .catch(err => {
          console.log("error", err);
          localStorage.removeItem("token");
          this.$router.push("/login");
        });
    },
    changeData($event) {
      console.log($event, "data");
      if ($event) {
        this.getAudio();
      }
    }
  },
  components: {
    Transcribe
  }
};
</script>

<style scoped></style>
