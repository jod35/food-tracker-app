const myHeaders = new Headers();

const requestOptions = {
  method: "GET",
  headers: myHeaders,
  vary: "Origin",
};

let promise = fetch("http:localhost:5000/", requestOptions);

promise.then(function (response) {
  console.log(response.json());

  response.json().then((data) => {
    console.log(data);
  });
});
