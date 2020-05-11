import getToken from "../utils/jwt";

function authGuard(to, from, next) {
  const token = localStorage.getItem("token");
  if (getToken(token)) {
    next();
  } else {
    next("/login");
  }
}

export default authGuard;
