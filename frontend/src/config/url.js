const BASE_URL = `http://localhost:8000`;

export const options = {
  headers: {
    Authorization:
      "JWT" + localStorage.getItem("token")
        ? localStorage.getItem("token")
        : "",
  },
};
export const SIGN_UP = `${BASE_URL}/api/signup/`;
export const LOGIN = `${BASE_URL}/api/login/`;
