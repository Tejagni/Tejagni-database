document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    
    // Get username and password
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Check if "Remember me" is checked
    var rememberMe = document.getElementById('remember-me').checked;

    // Set default username and password
    var defaultUsername = 'admin';
    var defaultPassword = '123user123';

    // Implement authentication logic here
    // For simplicity, let's assume authentication is successful if the entered credentials match the default ones
    var authenticated = (username === defaultUsername && password === defaultPassword);

    if (authenticated) {
        // Redirect to home.html
        window.location.href = 'home.html';
        
        // If "Remember me" is checked, store username and password in localStorage
        if (rememberMe) {
            localStorage.setItem('username', username);
            localStorage.setItem('password', password);
        } else {
            // If not checked, remove stored username and password from localStorage
            localStorage.removeItem('username');
            localStorage.removeItem('password');
        }
    } else {
        // Handle authentication failure, show error message, etc.
        alert('Invalid username or password');
    }
});

// Populate the form with stored username and password from localStorage, if available
window.onload = function() {
    var storedUsername = localStorage.getItem('username');
    var storedPassword = localStorage.getItem('password');

    if (storedUsername && storedPassword) {
        document.getElementById('username').value = storedUsername;
        document.getElementById('password').value = storedPassword;
    }
};
