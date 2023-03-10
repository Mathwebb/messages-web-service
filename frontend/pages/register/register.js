const form = document.getElementById('register-form');
form.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(form);

    body = {
        'name': formData.get('username'),
        'email_address': formData.get('email'),
    }

    console.log(body)

    fetch('http://localhost:8000/user', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(body),
    })
    .then(response => {
        if (response.ok) {
            response.json().then(data => {
                fetch('http://localhost:8000/user?email_address=' + formData.get('email'), {
                    method: 'GET'
                })
                .then(response => {
                    if (response.ok) {
                        response.json().then(data => {
                            sessionStorage.setItem('user', JSON.stringify(data));
                            window.location.href = 'http://localhost:8000/';
                        });
                    } else {
                        alert('Invalid email')
                        throw new Error('Unable to login');
                    }
                })
            });
        } else {
            alert('Invalid email')
            throw new Error('Unable to login');
        }
    })
    .catch(error => {
        alert('Invalid email')
        console.error(error);
    });
});
