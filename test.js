const requestOptions = {
    method: "GET",
    redirect: "follow"
};

fetch("https://5cbd-103-78-181-48.ngrok-free.app", {
    method: "GET",
    headers:{Authorization:'Token iloveyou', Accept:"application/json"}
})
    .then((response) => response.json())
    .then((result) => console.log(result))
    .catch((error) => console.error(error));