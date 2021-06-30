const translateBtn = document.getElementById("translate-btn");

translateBtn.addEventListener('click', () => {
  const inputText = document.getElementById("input-text").value;
  if(inputText != "") {
    const src = document.getElementById('src').value;
    const dest = document.getElementById("dest").value;
    eel.translate(inputText, src, dest);
  } else {
    alert("翻訳するテキストを入力してください。")
  }
})

eel.expose(displayText)
function displayText(translatedText) {
  document.getElementById("translated-text").value = translatedText;
}

const resetBtn = document.getElementById("reset-btn");
resetBtn.addEventListener('click', () => {
  document.getElementById("input-text").value = "";
  document.getElementById("translated-text").value = "";
})