<template>
  <div class="app">
    <Header :isAuthenticated="isAuthenticated" @setAuth="setAuth($event)"></Header>
    <div class="container routerView">
      <router-view @setAuth="setAuth($event)"></router-view>
    </div>
  </div>
</template>

<script>
import Header from "./components/header";
import getToken from "./utils/jwt";

export default {
  name: "App",
  data: function() {
    return {
      isAuthenticated: false
    };
  },
  components: {
    Header
  },
  created() {
    console.log("hello");
    const token = localStorage.getItem("token");
    if (!getToken(token)) {
      this.isAuthenticated = false;
      this.$router.push("/login");
    } else {
      this.isAuthenticated = true;
    }
  },
  methods: {
    setAuth(data) {
      console.log(data);
      this.isAuthenticated = data;
    }
  }
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #dbd0cc;
}

.routerView {
  margin-top: 65px;
}
</style>
