const sendButton = document.getElementById("send-btn");
const questionInput = document.getElementById("question");
const messages = document.getElementById("messages");

sendButton.addEventListener("click", function () {
    const question = questionInput.value.trim();
    // console.log(question);
    if(question == ""){
        return;
    }
    messages.innerHTML += "<div class='user-message'>You: " + question + "</div>";
    questionInput.value = "";
});