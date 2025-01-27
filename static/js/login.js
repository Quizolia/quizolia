// // document.addEventListener('DOMContentLoaded', () => {
// //     const darkModeToggle = document.getElementById('darkModeToggle');
// //     const body = document.body;
// //     const togglePassword = document.getElementById('togglePassword');
// //     const password = document.getElementById('password');
// //     const loginForm = document.getElementById('loginForm');
// //     const languageSelect = document.getElementById('languageSelect');

// //     // Dark mode toggle
// //     darkModeToggle.addEventListener('click', () => {
// //         body.classList.toggle('dark-mode');
// //     });

// //     // Password visibility toggle
// //     togglePassword.addEventListener('click', () => {
// //         const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
// //         password.setAttribute('type', type);
// //         togglePassword.classList.toggle('show');
// //     });

// //     // Form submission (prevent default for demo)
// //     loginForm.addEventListener('submit', (e) => {
// //         e.preventDefault();
// //         console.log('Form submitted');
// //     });

// //     // Language selection (demo - you would typically use a translation library)
// //     languageSelect.addEventListener('change', (e) => {
// //         console.log(`Language changed to: ${e.target.value}`);
// //     });

// //     // Subtle hover animation for buttons and links
// //     const interactiveElements = document.querySelectorAll('button, a');
// //     interactiveElements.forEach(element => {
// //         element.addEventListener('mouseenter', () => {
// //             element.style.transform = 'translateY(-2px)';
// //             element.style.transition = 'transform 0.3s ease';
// //         });
// //         element.addEventListener('mouseleave', () => {
// //             element.style.transform = 'translateY(0)';
// //         });
// //     });
// // });

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const loginForm = document.getElementById('loginForm');
//     const errorMessage = document.getElementById('error-message');
//     const passwordInput = document.getElementById('password');
//     const togglePassword = document.querySelector('.toggle-password');
//     const languageSelect = document.getElementById('languageSelect');

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

//     // Form validation and submission
//     loginForm.addEventListener('submit', async (e) => {
//         e.preventDefault();
//         const email = document.getElementById('email').value;
//         const password = passwordInput.value;

//         // Clear previous error messages
//         errorMessage.classList.add('hidden');
//         errorMessage.textContent = '';

//         try {
//             const response = await fetch('/login', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ email, password }),
//             });

//             const data = await response.json();

//             if (!response.ok) {
//                 throw new Error(data.message || 'Incorrect email or password.');
//             }

//             // Successful login
//             window.location.href = '/home';

//         } catch (error) {
//             // Show error message
//             errorMessage.textContent = error.message;
//             errorMessage.classList.remove('hidden');
//             errorMessage.classList.add('show');

//             // Add shake animation to form
//             loginForm.classList.add('shake');
//             setTimeout(() => loginForm.classList.remove('shake'), 500);
//         }
//     });

//     // Language selection
//     languageSelect.addEventListener('change', (e) => {
//         const selectedLanguage = e.target.value;
//         localStorage.setItem('preferredLanguage', selectedLanguage);
//         // You would typically implement language switching logic here
//     });

//     // Load saved language preference
//     const savedLanguage = localStorage.getItem('preferredLanguage');
//     if (savedLanguage) {
//         languageSelect.value = savedLanguage;
//     }

//     // Subtle hover animation for buttons and links
//     const interactiveElements = document.querySelectorAll('button, a');
//     interactiveElements.forEach(element => {
//         element.addEventListener('mouseenter', () => {
//             element.style.transform = 'translateY(-2px)';
//             element.style.transition = 'transform 0.3s ease';
//         });
//         element.addEventListener('mouseleave', () => {
//             element.style.transform = 'translateY(0)';
//         });
//     });
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
                showFlashMessage('An error occurred. Please try again.');
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
                showFlashMessage('An error occurred. Please try again.');
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