<template>
  <div>
    <h2>Login</h2>
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
        </div>
      </div>

      <button type="button" class="btn btn-primary" @click.prevent="submitData">Submit</button>
      <div class="alert alert-danger mt-2" v-if="error">{{errorMessage}}</div>
    </form>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import axios from "axios";
import { LOGIN } from "../config/url";
export default {
  name: "Login",
  data: function() {
    return {
      user: {
        username: "",
        password: ""
      },
      submitted: false,
      error: false,
      errorMessage: ""
    };
  },
  validations: {
    user: {
      username: { required },
      password: { required }
    }
  },
  methods: {
    submitData() {
      this.submitted = true;
      this.error = false;
      this.errorMessage = "";

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
        .post(LOGIN, data)
        .then(responseData => {
          console.log(responseData.data.token);
          localStorage.setItem("token", responseData.data.token);
          this.$router.push("/home");
        })
        .catch(err => {
          console.log("err", err);
          this.error = true;
          this.errorMessage = "please enter valid credentials";
        });
    }
  }
};
</script>

<style scoped></style>
