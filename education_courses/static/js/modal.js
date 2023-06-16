// Открыть модальное окно при клике на кнопку
document.getElementById("openModal").addEventListener("click", function () {
  document.getElementById("myModal").style.display = "block";
});

// Закрыть модальное окно при клике на крестик
document.getElementsByClassName("close")[0].addEventListener("click", function () {
  document.getElementById("myModal").style.display = "none";
});

// Закрыть модальное окно при клике вне окна
window.addEventListener("click", function (event) {
  if (event.target == document.getElementById("myModal")) {
    document.getElementById("myModal").style.display = "none";
  }
});

function updateInputValue() {
  var costValue = document.getElementById("costId").innerText;
  var formattedValue = costValue.replace(" ₽/мес", "");
  var inputElement = document.getElementById("valueMain");
  inputElement.value = formattedValue;
}

window.addEventListener("load", updateInputValue);