const user = JSON.parse(sessionStorage.getItem('user'));

if (!user) {
  window.alert('You must be logged in to view your messages');
  window.location.href = '/login';
}

email = user.email
username = user.name

document.getElementById('username').textContent = username;
document.getElementById('email').textContent = email;

fetch('http://localhost:8000/message?sender_email=' + email)
.then(response => response.json())
.then(messages => {
    const messageList = document.getElementById('sent-messages-list');
    messages.forEach(message => {
        const listItem = document.createElement('li');
        listItem.id = `message-${message.id}`;
        const receiver = message.recipient_email;
        const subject = message.subject;
        const to = document.createElement('p');
        const sub = document.createElement('p');
        to.textContent = `To: ${receiver}`;
        sub.textContent = `Subject: ${subject}`;
        const deleteButton = document.createElement('button');
        const viewButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        viewButton.textContent = 'View';
        deleteButton.onclick = () => deleteMessage(message.id);
        viewButton.onclick = () => window.location.href = `/message/${message.id}`;
        listItem.appendChild(to);
        listItem.appendChild(sub);
        listItem.appendChild(document.createElement('br'));
        listItem.appendChild(deleteButton);
        listItem.appendChild(viewButton);
        messageList.appendChild(listItem);
    });
})
.catch(error => {
    console.error(error);
});

fetch('http://localhost:8000/message?recipient_email=' + email)
.then(response => response.json())
.then(messages => {
    const messageList = document.getElementById('received-messages-list');
    messages.forEach(message => {
        const listItem = document.createElement('li');
        listItem.id = `message-${message.id}`;
        const sender = message.sender_email;
        const subject = message.subject;
        const from = document.createElement('p');
        const sub = document.createElement('p');
        from.textContent = `From: ${sender}`;
        sub.textContent = `Subject: ${subject}`;
        const viewButton = document.createElement('button');
        viewButton.textContent = 'View';
        viewButton.onclick = () => window.location.href = `/message/${message.id}`;
        listItem.appendChild(from);
        listItem.appendChild(sub);
        listItem.appendChild(document.createElement('br'));
        listItem.appendChild(viewButton)
        messageList.appendChild(listItem);
    });
})
.catch(error => {
    console.error(error);
});

function deleteMessage(messageId) {
    fetch(`/message?message_id=${messageId}`, { method: 'DELETE' })
      .then(response => {
        if (response.ok) {
          const listItem = document.getElementById(`message-${messageId}`);
          listItem.parentNode.removeChild(listItem);
        } else {
          throw new Error('Unable to delete message');
        }
      })
      .catch(error => {
        console.error(error);
      });
  }
