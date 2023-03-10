const form = document.getElementById('login-form');
form.addEventListener('submit', event => {
    event.preventDefault();

    const formData = new FormData(form);

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
    .catch(error => {
        alert('Invalid email')
        console.error(error);
    });
});

function signupRedirect() {
    window.location.href = 'http://localhost:8000/register';
}
