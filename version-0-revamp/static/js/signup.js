// // document.addEventListener('DOMContentLoaded', () => {
// //     const darkModeToggle = document.getElementById('darkModeToggle');
// //     const body = document.body;

// //     // Check for saved theme preference or default to light mode
// //     const currentTheme = localStorage.getItem('theme');
// //     if (currentTheme) {
// //         body.classList.add(currentTheme);
// //     }

// //     // Dark mode toggle
// //     darkModeToggle.addEventListener('click', () => {
// //         body.classList.toggle('dark-mode');
// //         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
// //     });
// // });

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const signupForm = document.getElementById('signupForm');
//     const errorMessage = document.getElementById('error-message');
//     const passwordInput = document.getElementById('password');
//     const togglePassword = document.querySelector('.toggle-password');
//     const passwordRequirements = document.querySelector('.password-requirements');

//     // Password validation requirements
//     const requirements = {
//         length: { regex: /.{8,}/, element: document.getElementById('length-check') },
//         number: { regex: /\d/, element: document.getElementById('number-check') },
//         uppercase: { regex: /[A-Z]/, element: document.getElementById('uppercase-check') },
//         lowercase: { regex: /[a-z]/, element: document.getElementById('lowercase-check') },
//         special: { regex: /[!@#$%^&*]/, element: document.getElementById('special-check') }
//     };

//     // Load saved theme
//     const savedTheme = localStorage.getItem('theme');
//     if (savedTheme) {
//         body.classList.add(savedTheme);
//     }

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
//     });

//     // Password visibility toggle
//     togglePassword.addEventListener('click', () => {
//         const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
//         passwordInput.setAttribute('type', type);
//         togglePassword.querySelector('.eye-icon').classList.toggle('hidden');
//         togglePassword.querySelector('.eye-off-icon').classList.toggle('hidden');
//     });

//     // Password validation
//     passwordInput.addEventListener('focus', () => {
//         passwordRequirements.classList.remove('hidden');
//     });

//     passwordInput.addEventListener('input', () => {
//         const password = passwordInput.value;
//         let isValid = true;

//         // Check each requirement
//         Object.entries(requirements).forEach(([key, requirement]) => {
//             const valid = requirement.regex.test(password);
//             requirement.element.classList.toggle('valid', valid);
//             if (!valid) isValid = false;
//         });

//         // Update password input styling
//         passwordInput.classList.toggle('invalid-input', !isValid);
//     });

//     passwordInput.addEventListener('blur', () => {
//         if (passwordInput.value === '') {
//             passwordRequirements.classList.add('hidden');
//         }
//     });

//     // Form validation and submission
//     signupForm.addEventListener('submit', async (e) => {
//         e.preventDefault();

//         // Get form data
//         const formData = new FormData(signupForm);
//         const userData = Object.fromEntries(formData.entries());

//         // Validate password
//         let isValid = true;
//         Object.values(requirements).forEach(requirement => {
//             if (!requirement.regex.test(userData.password)) {
//                 isValid = false;
//             }
//         });

//         if (!isValid) {
//             showError('Please ensure your password meets all requirements.');
//             return;
//         }

//         try {
//             const response = await fetch('/signup', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify(userData),
//             });

//             const data = await response.json();

//             if (!response.ok) {
//                 throw new Error(data.message || 'Email already exists in our records.');
//             }

//             // Successful signup
//             window.location.href = '/login';

//         } catch (error) {
//             showError(error.message);
//         }
//     });

//     function showError(message) {
//         errorMessage.textContent = message;
//         errorMessage.classList.remove('hidden');
//         errorMessage.classList.add('show');

//         // Add shake animation to form
//         signupForm.classList.add('shake');
//         setTimeout(() => signupForm.classList.remove('shake'), 500);
//     }
// });

document.addEventListener('DOMContentLoaded', () => {
    // Form validation and submission
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const passwordToggles = document.querySelectorAll('.password-toggle');

    // Password visibility toggle
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            const button = e.currentTarget;
            const input = button.previousElementSibling;
            const type = input.type === 'password' ? 'text' : 'password';
            input.type = type;
            button.classList.toggle('showing');
        });
    });

    // Password validation
    const passwordValidation = {
        length: (password) => password.length >= 8,
        number: (password) => /\d/.test(password),
        special: (password) => /[!@#$%^&*(),.?":{}|<>]/.test(password),
        case: (password) => /[a-z]/.test(password) && /[A-Z]/.test(password)
    };

    function validatePassword(password) {
        const checks = {
            lengthCheck: passwordValidation.length(password),
            numberCheck: passwordValidation.number(password),
            specialCheck: passwordValidation.special(password),
            caseCheck: passwordValidation.case(password)
        };

        // Update UI for each requirement
        Object.entries(checks).forEach(([id, valid]) => {
            const element = document.getElementById(id);
            if (element) {
                element.classList.toggle('valid', valid);
            }
        });

        return Object.values(checks).every(Boolean);
    }

    // Show error message
    function showError(element, message) {
        const errorDiv = document.getElementById(`${element.id}Error`);
        if (errorDiv) {
            errorDiv.textContent = message;
            errorDiv.classList.add('visible');
        }
    }

    // Clear error message
    function clearError(element) {
        const errorDiv = document.getElementById(`${element.id}Error`);
        if (errorDiv) {
            errorDiv.textContent = '';
            errorDiv.classList.remove('visible');
        }
    }

    // Flash message
    function showFlashMessage(message, type = 'error') {
        const flashDiv = document.createElement('div');
        flashDiv.className = `flash-message ${type}`;
        flashDiv.textContent = message;
        document.body.appendChild(flashDiv);

        setTimeout(() => {
            flashDiv.remove();
        }, 5000);
    }

    // Signup form validation
    if (signupForm) {
        const passwordInput = signupForm.querySelector('input[name="password"]');
        
        passwordInput.addEventListener('input', (e) => {
            const isValid = validatePassword(e.target.value);
            clearError(passwordInput);
            if (!isValid) {
                showError(passwordInput, 'Please meet all password requirements');
            }
        });

        signupForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(signupForm);
            const password = formData.get('password');

            if (!validatePassword(password)) {
                showError(passwordInput, 'Please meet all password requirements');
                return;
            }

            try {
                const response = await fetch('/signup', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (response.ok) {
                    window.location.href = '/login';
                } else {
                    if (data.error === 'email_exists') {
                        showError(signupForm.querySelector('input[name="email"]'), 'Email already exists');
                    } else {
                        showFlashMessage('An error occurred. Please try again.');
                    }
                }
            } catch (error) {
                showFlashMessage('SignUp!! An error occurred. Please try again.');
            }
        });
    }

    // Login form validation
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(loginForm);

            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (response.ok) {
                    window.location.href = '/home';
                } else {
                    showFlashMessage('Incorrect email or password.');
                }
            } catch (error) {
                showFlashMessage('Login!! An occurred. Please try again.');
            }
        });
    }

    // Dark mode toggle (existing functionality)
    const darkModeToggle = document.getElementById('darkModeToggle');
    if (darkModeToggle) {
        darkModeToggle.addEventListener('click', () => {
            document.body.classList.toggle('dark-mode');
            localStorage.setItem('theme', 
                document.body.classList.contains('dark-mode') ? 'dark' : 'light'
            );
        });
    }
});