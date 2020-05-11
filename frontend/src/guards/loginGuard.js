import getToken from "../utils/jwt";

function loginGuard(to, from, next) {
  const token = localStorage.getItem("token");
  if (getToken(token)) {
    next("/");
  } else {
    next();
  }
}

export default loginGuard;
