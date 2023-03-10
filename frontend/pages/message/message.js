const message_id = window.location.href.split('/')[4];

const user_email = JSON.parse(sessionStorage.getItem('user')).email;
console.log(user_email);

const sender_email = document.getElementById('sender-email');
console.log(sender_email.textContent);

if (sender_email.textContent === user_email) {
    document.getElementById('reply-btn').style.display = 'none';
}

function returnHome() {
    window.location.href = '/';
}

function replyMessage() {
    window.location.href = `http://localhost:8000/message/${message_id}/reply`;
}

function forwardMessage() {
    window.location.href = `http://localhost:8000/message/${message_id}/forward`;
}
