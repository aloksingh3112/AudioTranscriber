<template>
  <div>
    <h2>Signup</h2>
    <hr />
    <form>
      <div class="form-group">
        <label for="username">Username</label>
        <input
          type="text"
          v-model="user.username"
          id="username"
          name="username"
          class="form-control"
          :class="{ 'is-invalid': submitted && $v.user.username.$error }"
        />
        <div
          v-if="submitted && !$v.user.username.required"
          class="invalid-feedback"
        >username is required</div>
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          v-model="user.password"
          id="password"
          name="password"
          class="form-control"
          :class="{ 'is-invalid': submitted && $v.user.password.$error }"
        />
        <div v-if="submitted && $v.user.password.$error" class="invalid-feedback">
          <span v-if="!$v.user.password.required">Password is required</span>
          <span v-if="!$v.user.password.minLength">Password must be at least 6 characters</span>
        </div>
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input
          type="email"
          v-model="user.email"
          id="email"
          name="email"
          class="form-control"
          :class="{ 'is-invalid': submitted && $v.user.email.$error }"
        />
        <div v-if="submitted && $v.user.email.$error" class="invalid-feedback">
          <span v-if="!$v.user.email.required">Email is required</span>
          <span v-if="!$v.user.email.email">Email is invalid</span>
        </div>
      </div>
      <button type="button" class="btn btn-primary" @click.prevent="submitData">Submit</button>
      <div class="alert alert-danger mt-2" v-if="error">{{errorMessage}}</div>
    </form>
  </div>
</template>

<script>
import { required, email, minLength } from "vuelidate/lib/validators";
import axios from "axios";
import { SIGN_UP } from "../config/url";
import getToken from "../utils/jwt";

export default {
  name: "Signup",
  data: function() {
    return {
      user: {
        username: "",
        password: "",
        email: ""
      },
      submitted: false,
      error: false,
      errorMessage: ""
    };
  },
  validations: {
    user: {
      username: { required },
      email: { required, email },
      password: { required, minLength: minLength(6) }
    }
  },
  methods: {
    submitData() {
      this.error = false;
      this.errorMessage = "";
      this.submitted = true;

      this.$v.$touch();
      if (this.$v.$invalid) {
        return;
      }
      console.log(this.user);
      const data = {
        username: this.user.username,
        password: this.user.password,
        email: this.user.email
      };
      axios
        .post(SIGN_UP, data)
        .then(responseData => {
          console.log(responseData);

          localStorage.setItem("token", responseData.data.data.token);
          this.$emit("setAuth", true);
          this.$router.push("/");
        })
        .catch(err => {
          console.log("err", err.response);
          this.error = true;
          this.errorMessage = err.response
            ? err.response.data.message
            : "Something went wrong";
        });
    }
  },
  created() {
    const token = localStorage.getItem("token");
    if (getToken(token)) {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped></style>
