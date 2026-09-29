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

    messages.innerHTML += "<div class='bot-message' id='loading'>Bot is thinking...</div>";

    fetch("http://127.0.0.1:8000/ask",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body:JSON.stringify({
            question: question
        })
    })
    .then(response => response.json())
    // .then(data => console.log(data));
    .then(data => {
        // console.log(data.sources);
        document.getElementById("loading").remove();

        messages.innerHTML += "<div class='bot-message'>Bot: " + data.answer +"</div>";

        messages.innerHTML +="<div class='sources-title'>Sources</div>";

            data.sources.forEach(function (source) {
            messages.innerHTML +=
                "<div class='source-message'>Source: " +
                source.source +
                " | Page: " +
                source.page +
                "</div>";
            });
        })
        .catch(function () {
            document.getElementById("loading").remove();

            messages.innerHTML += "<div class='bot-message'>Sorry something went wrong. Please try again.</div>";
        });
    });