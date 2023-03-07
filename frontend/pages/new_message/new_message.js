const userEmail = JSON.parse(sessionStorage.getItem('user')).email;

document.getElementById('sender-email').value = userEmail;

const form = document.getElementById('new-message')
form.addEventListener('submit', event =>{
  event.preventDefault();

  const recipientEmail = document.getElementById('recipient-email').value;
  const subject = document.getElementById('subject').value;
  const body = document.getElementById('body').value;

  const message = {
    sender_email: userEmail,
    recipient_email: recipientEmail,
    subject: subject,
    body: body
  };

  fetch('/message', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(message)
  })
  .then(response => {
    if (response.ok) {
      alert('Message sent successfully!');
      window.location.href = '/';
    } else {
      alert('Error sending message.');
    }
  })
  .catch(error => {
    console.error(error);
    alert('Arbitrary error.');
  });
});
