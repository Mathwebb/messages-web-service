message_id = window.location.href.split('/')[4];
const user_email = JSON.parse(sessionStorage.getItem('user')).email;

function returnHome() {
    window.location.href = '/';
}

fetch('/message?message_id=' + message_id, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => {
    if (response.ok) {
        response.json().then(data => {
            document.getElementById('sender-email').value = user_email;
            document.getElementById('subject').value = data.subject;
            document.getElementById('body').value = data.body;
        });
    } else {
        alert('Unable to retrieve message');
        throw new Error('Unable to retrieve message');
    }
}).catch(error => {
    alert('Unable to retrieve message');
    console.error(error);
});

const form = document.getElementById('forward-form');

form.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(document.getElementById('forward-form'));

    fetch('/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            sender_email: formData.get('sender-email'),
            recipient_email: formData.get('recipient-email'),
            subject: formData.get('subject'),
            body: formData.get('body')
        })
    }).then(response => {
        if (response.ok) {
            window.location.href = '/message/' + message_id;
        } else {
            alert('Unable forward message');
            throw new Error('Unable forward message');
        }
    }).catch(error => {
        alert('Unable forward message');
        console.error(error);
    });
});
