document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Page refresh hone se rokna

    // Inputs aur Error spans ko get karna
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const role = document.getElementById('role').value;

    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    const roleError = document.getElementById('roleError');
    const messageBox = document.getElementById('messageBox');

    // Pehle sab errors clear karein
    emailError.textContent = '';
    passwordError.textContent = '';
    roleError.textContent = '';
    document.getElementById('email').classList.remove('input-error');
    document.getElementById('password').classList.remove('input-error');
    document.getElementById('role').classList.remove('input-error');
    messageBox.className = 'message-box';
    messageBox.style.display = 'none';

    let isValid = true;

    // TC04: Empty email and password (Validation error)
    if (email === '') {
        emailError.textContent = 'Email is required.';
        document.getElementById('email').classList.add('input-error');
        isValid = false;
    }
    if (password === '') {
        passwordError.textContent = 'Password is required.';
        document.getElementById('password').classList.add('input-error');
        isValid = false;
    }
    if (role === '') {
        roleError.textContent = 'Please select a role.';
        document.getElementById('role').classList.add('input-error');
        isValid = false;
    }

    // TC05: Invalid email format (Validation error)
    // Simple regex format check
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (email !== '' && !email.match(emailPattern)) {
        emailError.textContent = 'Please enter a valid email address.';
        document.getElementById('email').classList.add('input-error');
        isValid = false;
    }

    // Agar basic validation fail ho jaye to yahin ruk jayein
    if (!isValid) return;

    // ==========================================
    // MOCK BACKEND LOGIC (Jab tak asli backend nahi banta)
    // ==========================================
    
    // Hamara Nakli Database (Fake Account)
    const correctEmail = "admin@lms.com";
    const correctPassword = "123456";

    // TC03: Email not registered (Login rejected)
    if (email !== correctEmail) {
        messageBox.textContent = 'Error: Email is not registered in our system.';
        messageBox.classList.add('msg-error');
        return;
    }

    // TC02: Incorrect password (Login rejected)
    if (password !== correctPassword) {
        messageBox.textContent = 'Error: Incorrect password. Please try again.';
        messageBox.classList.add('msg-error');
        return;
    }

    // TC01: Valid email and password (Login successful)
    messageBox.textContent = `Success! Welcome ${role.toUpperCase()}. Redirecting to dashboard...`;
    messageBox.classList.add('msg-success');
    
    // Form clear kar dein
    document.getElementById('loginForm').reset();
});