
const chat_container = document.querySelector('.chatbot-container');
const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');

const floating_chat = document.getElementById('floating_chat');
floating_chat.addEventListener('click', function () {
    chat_container.style.display = 'block';
    chat_circle.style.display = 'none';
})
const header_close = document.getElementById('chat_close');
chat_close.addEventListener('click', function () {
    chat_container.style.display = 'none';
    chat_circle.style.display = 'block';
})


inputForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const input = inputField.value;

    inputField.value = '';
    const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: "2-digit" });

    let message = document.createElement('div');
    message.classList.add('chatbot-message', 'user-message');
    message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${input}</p>`;
    conversation.appendChild(message);

    generateResponse(input)
        .then(response => {
            message = document.createElement('div');
            message.classList.add('chatbot-message', 'chatbot');
            message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${response['response']}</p>`;
            conversation.appendChild(message);
            message.scrollIntoView({ behavior: "smooth" });
        })
        .catch(error => {
            console.error(error);
        });
});
// 추후에 api로 수정

