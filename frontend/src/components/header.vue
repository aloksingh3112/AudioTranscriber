<template>
  <nav class="navbar fixed-top header d-flex justify-content-between">
    <div>
      <router-link to="/" class="navbar-brand text-dark font-weight-bold">Audio Transcriber</router-link>
    </div>
    <div>
      <router-link
        to="/login"
        class="navbar-brand text-dark font-weight-bold links"
        v-if="!isAuthenticated"
      >Login</router-link>
      <router-link
        to="/signup"
        class="navbar-brand text-dark font-weight-bold links"
        v-if="!isAuthenticated"
      >Signup</router-link>
      <a
        class="navbar-brand text-dark font-weight-bold links"
        v-if="isAuthenticated"
        v-on:click="logout"
      >logout</a>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Header",
  props: {
    isAuthenticated: Boolean
  },

  methods: {
    logout() {
      this.$emit("setAuth", false);
      localStorage.removeItem("token");
      this.$router.push("/login");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  background-color: #c1aea8;
}
.links {
  text-decoration: underline;
  cursor: pointer;
}
</style>
