import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/home";
import Login from "../components/login";
import Signup from "../components/signup";

Vue.use(VueRouter);

const router = new VueRouter({
  routes: [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/login",
      component: Login,
    },
    {
      path: "/signup",
      component: Signup,
    },
  ],
  mode: "history",
});

export default router;
