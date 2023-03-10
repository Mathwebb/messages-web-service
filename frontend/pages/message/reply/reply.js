message_id = window.location.href.split('/')[4];

fetch('/message?message_id=' + message_id, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    }
}).then(response => {
    if (response.ok) {
        response.json().then(data => {
            console.log(data);
            document.getElementById('sender-email').value = data.recipient_email;
            document.getElementById('recipient-email').value = data.sender_email;
            document.getElementById('subject').value = data.subject;
        });
    } else {
        alert('Unable to retrieve message');
        throw new Error('Unable to retrieve message');
    }
}).catch(error => {
    alert('Unable to retrieve message');
    console.error(error);
});

function returnHome() {
    window.location.href = '/';
}

const form = document.getElementById('reply-form');

form.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(document.getElementById('reply-form'));

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
            alert('Unable to send reply');
            throw new Error('Unable to send reply');
        }
    }).catch(error => {
        alert('Unable to send reply');
        console.error(error);
    });
});