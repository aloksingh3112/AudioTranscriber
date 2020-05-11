<template>
  <nav class="navbar fixed-top header d-flex justify-content-between">
    <div>
      <router-link to="/" class="navbar-brand text-dark font-weight-bold">Audio Transcriber</router-link>
    </div>
    <div>
      <router-link
        to="/login"
        class="navbar-brand text-dark font-weight-bold links"
        v-if="!isAuth"
      >Login</router-link>
      <router-link
        to="/signup"
        class="navbar-brand text-dark font-weight-bold links"
        v-if="!isAuth"
      >Signup</router-link>
      <a class="navbar-brand text-dark font-weight-bold links" v-if="isAuth">logout</a>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Header",
  props: {
    isAuthenticated: Boolean
  },
  data: function() {
    return {
      isAuth: this.isAuthenticated
    };
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
