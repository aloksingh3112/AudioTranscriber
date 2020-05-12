<template>
  <div class="card mt-4 p-2 shadow-lg" v-bind:key="item.id" v-if="!item.isTranscribed">
    <div class="card-body">
      <h4>
        {{item.title}}
        <span></span>
      </h4>
      <audio controls>
        <source v-bind:src="item.audioLink" type="audio/flac" />
      </audio>
      <div class="mt-3" v-if="id==item.id && isClicked">
        <div class="form-group">
          <label for="td">Transcribe Audio Here</label>
          <textarea
            class="form-control"
            id="td"
            rows="4"
            v-model="data.audioValue"
            :class="{ 'is-invalid': submitted && $v.data.audioValue.$error }"
          ></textarea>
          <div
            v-if="submitted && !$v.data.audioValue.required"
            class="invalid-feedback"
          >Transcribtion is required</div>
        </div>
        <button class="btn btn-secondary" v-on:click="submitData(item)">Submit</button>
      </div>
    </div>
    <div class="card-footer">
      <button
        class="btn btn-primary"
        v-on:click="transcribeTogle(item.id)"
      >{{isClicked?"Toggle View ":"Click Here To Start Transcribing Audio"}}</button>
    </div>
  </div>
</template>

<script>
import Axios from "axios";
import { required } from "vuelidate/lib/validators";
import { ADD_TRANSCRIBE } from "../config/url";
export default {
  name: "Transcribe",
  data: function() {
    return {
      id: 0,
      isClicked: false,
      data: {
        audioValue: ""
      },
      submitted: false
    };
  },
  validations: {
    data: {
      audioValue: { required }
    }
  },
  props: {
    item: Object
  },

  methods: {
    transcribeTogle: function(id) {
      this.id = id;
      this.isClicked = !this.isClicked;
    },
    submitData: function(item) {
      this.submitted = true;

      this.$v.$touch();
      if (this.$v.$invalid) {
        return;
      }
      const data = {
        id: item.id,
        title: item.title,
        audioLink: item.audioLink,
        transcribedData: this.data.audioValue,
        isTranscribed: true
      };
      const OPTIONS = {
        headers: {
          Authorization: localStorage.getItem("token")
            ? "JWT" + " " + localStorage.getItem("token")
            : ""
        }
      };
      Axios.post(ADD_TRANSCRIBE, data, OPTIONS)
        .then(responseData => {
          console.log(responseData);
          alert(responseData.data.message);
          this.$emit("changeData", true);
        })
        .catch(err => {
          alert(err.response.data.message);
        });
    }
  }
};
</script>

<style scoped>
textarea {
  resize: none;
}
</style>
