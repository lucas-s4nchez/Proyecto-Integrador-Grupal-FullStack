const inputNombre = document.getElementById("name");
const inputEmail = document.getElementById("email");
const inputText = document.getElementById("textarea");
const form = document.getElementById("message-form");
const btnSubmit = document.getElementById("btn-enviar");

const checkName = () => {
  let valid = false;
  const min = 3;
  const max = 25;
  const nombre = inputNombre.value.trim();
  // verificamos si el campo esta ok o no
  if (isEmpty(nombre)) {
    showError(inputNombre, "El nombre es obligatorio"); // va a mostrar mi mensaje de error
  } else if (!isBetween(nombre.length, min, max)) {
    showError(
      inputNombre,
      `El nombre debe tener entre ${min} y ${max} caracteres`
    );
  } else {
    showSuccess(inputNombre); // va a mostrar mi mensaje de exito
    valid = true;
  }
  return valid;
};

const checkEmail = () => {
  let valid = false;
  const email = inputEmail.value.trim();
  if (isEmpty(email)) {
    showError(inputEmail, "El email es obligatorio");
  } else if (!isEmailValid(email)) {
    // checkeamos si el email es valido o no
    showError(inputEmail, "El email no es valido");
  } else {
    showSuccess(inputEmail); // va a mostrar mi mensaje de exito
    valid = true;
  }
  return valid;
};

const checkMessage = () => {
  let valid = false;

  const min = 3;
  const max = 150;
  const message = inputText.value.trim();
  // verificamos si el campo esta ok o no
  if (isEmpty(message)) {
    showError(inputText, "El mensaje es obligatorio"); // va a mostrar mi mensaje de error
  } else if (!isBetween(message.length, min, max)) {
    showError(
      inputText,
      `El mensaje debe tener entre ${min} y ${max} caracteres`
    );
  } else {
    showSuccess(inputText); // va a mostrar mi mensaje de exito
    valid = true;
  }
  return valid;
};

// creamos la funcion para validar si un campo esta vacio
const isEmpty = (value) => value === "";
// creamos la funcion para validar si un campo numerico esta entre los valores dados por min y max
const isBetween = (length, min, max) =>
  length < min || length > max ? false : true;
// creamos la funcion para validar si un email es valido
const isEmailValid = (email) => {
  const re =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  //testear
  return re.test(email);
};

//funcion para mostrar el error
// recibir el input y el msg de error
const showError = (input, message) => {
  const formField = input.parentElement;
  formField.classList.remove("success");
  formField.classList.add("error");
  const error = formField.querySelector("small");
  error.textContent = message;
};
const showSuccess = (input) => {
  const formField = input.parentElement;
  formField.classList.remove("error");
  formField.classList.add("success");
  const error = formField.querySelector("small");
  error.textContent = "";
};

const submit = (form) => {
  form.submit();
};
const validateForm = (e) => {
  e.preventDefault();

  // guardar el estado de los inputs en variables
  let isNameValid = checkName();
  let isEmailValid = checkEmail();
  let isMessageValid = checkMessage();

  let isFormValid = isNameValid && isEmailValid && isMessageValid;

  if (isFormValid) {
    console.log("valido");
    submit(form);
  }
};

inputNombre.addEventListener("keyup", checkName);
inputNombre.addEventListener("blur", checkName);
inputEmail.addEventListener("keyup", checkEmail);
inputEmail.addEventListener("blur", checkEmail);
inputText.addEventListener("keyup", checkMessage);
inputText.addEventListener("blur", checkMessage);
btnSubmit.addEventListener("click", validateForm);
