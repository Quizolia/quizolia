// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;

//     // Check for saved theme preference or default to light mode
//     const currentTheme = localStorage.getItem('theme');
//     if (currentTheme) {
//         body.classList.add(currentTheme);
//     }

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
//     });
// });


// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;

//     // Check for saved theme preference or default to light mode
//     const currentTheme = localStorage.getItem('theme');
//     if (currentTheme) {
//         body.classList.add(currentTheme);
//     }

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
//     });

//     // Password visibility toggle
//     const passwordToggles = document.querySelectorAll('.password-toggle');
    
//     passwordToggles.forEach(toggle => {
//         toggle.addEventListener('click', (e) => {
//             const button = e.currentTarget;
//             const passwordField = button.parentElement.querySelector('input');
//             const eyeIcon = button.querySelector('.eye-icon');
//             const eyeOffIcon = button.querySelector('.eye-off-icon');

//             // Toggle password visibility
//             const type = passwordField.type === 'password' ? 'text' : 'password';
//             passwordField.type = type;

//             // Toggle icons
//             eyeIcon.classList.toggle('hidden');
//             eyeOffIcon.classList.toggle('hidden');

//             // Update aria-label
//             button.setAttribute('aria-label', 
//                 type === 'password' ? 'Show password' : 'Hide password'
//             );
//         });
//     });
// });

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const form = document.querySelector('.form__container');
//     const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
//     const passwordInput = document.getElementById('password');
//     const passwordRequirements = document.querySelector('.password-requirements');

//     // Password validation patterns
//     const passwordPatterns = {
//         length: /.{8,}/,
//         lowercase: /[a-z]/,
//         uppercase: /[A-Z]/,
//         number: /[0-9]/
//     };

//     // Dark mode functionality
//     const currentTheme = localStorage.getItem('theme');
//     if (currentTheme) {
//         body.classList.add(currentTheme);
//     }

//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
//     });

//     // Prevent whitespace in inputs
//     inputs.forEach(input => {
//         input.addEventListener('input', (e) => {
//             // Remove whitespace as user types
//             e.target.value = e.target.value.replace(/\s/g, '');
//         });

//         input.addEventListener('blur', (e) => {
//             // Trim whitespace on blur
//             e.target.value = e.target.value.trim();
//         });
//     });

//     // Password validation
//     function validatePassword(password) {
//         const checks = {
//             length: passwordPatterns.length.test(password),
//             lowercase: passwordPatterns.lowercase.test(password),
//             uppercase: passwordPatterns.uppercase.test(password),
//             number: passwordPatterns.number.test(password)
//         };

//         // Update requirement indicators
//         document.getElementById('length-check').classList.toggle('valid', checks.length);
//         document.getElementById('lowercase-check').classList.toggle('valid', checks.lowercase);
//         document.getElementById('uppercase-check').classList.toggle('valid', checks.uppercase);
//         document.getElementById('number-check').classList.toggle('valid', checks.number);

//         // Update input styling
//         passwordInput.classList.toggle('valid', Object.values(checks).every(Boolean));
//         passwordInput.classList.toggle('invalid', !Object.values(checks).every(Boolean));

//         return Object.values(checks).every(Boolean);
//     }

//     // Password visibility toggle
//     const passwordToggles = document.querySelectorAll('.password-toggle');
    
//     passwordToggles.forEach(toggle => {
//         toggle.addEventListener('click', (e) => {
//             const button = e.currentTarget;
//             const passwordField = button.parentElement.querySelector('input');
//             const eyeIcon = button.querySelector('.eye');
//             const eyeOffIcon = button.querySelector('.eye-off');

//             // Toggle password visibility
//             const type = passwordField.type === 'password' ? 'text' : 'password';
//             passwordField.type = type;

//             // Toggle icons
//             eyeIcon.classList.toggle('hidden');
//             eyeOffIcon.classList.toggle('hidden');

//             // Update aria-label
//             button.setAttribute('aria-label', 
//                 type === 'password' ? 'Show password' : 'Hide password'
//             );
//         });
//     });

//     // Real-time password validation
//     passwordInput.addEventListener('input', (e) => {
//         validatePassword(e.target.value);
//     });

//     // Form submission
//     form.addEventListener('submit', (e) => {
//         e.preventDefault();
        
//         // Validate all fields
//         let isValid = true;
        
//         // Check for empty fields
//         inputs.forEach(input => {
//             if (!input.value.trim()) {
//                 isValid = false;
//                 showError(input, 'This field is required');
//             } else {
//                 clearError(input);
//             }
//         });

//         // Validate password
//         if (!validatePassword(passwordInput.value)) {
//             isValid = false;
//             showError(passwordInput, 'Please meet all password requirements');
//         }

//         // If all validations pass, submit the form
//         if (isValid) {
//             form.submit();
//         }
//     });

//     // Helper functions
//     function showError(input, message) {
//         const errorDiv = input.parentElement.querySelector('.error-message') || 
//                         createErrorElement(input);
//         errorDiv.textContent = message;
//         errorDiv.classList.add('visible');
//         input.classList.add('invalid');
//     }

//     function clearError(input) {
//         const errorDiv = input.parentElement.querySelector('.error-message');
//         if (errorDiv) {
//             errorDiv.classList.remove('visible');
//         }
//         input.classList.remove('invalid');
//     }

//     function createErrorElement(input) {
//         const errorDiv = document.createElement('div');
//         errorDiv.className = 'error-message';
//         input.parentElement.appendChild(errorDiv);
//         return errorDiv;
//     }
// });

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const form = document.querySelector('.form__container');
    const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"]');
    const passwordInput = document.getElementById('password');
    const emailInput = document.getElementById('mail');
    const passwordRequirements = document.querySelector('.password-requirements');

    // Password validation patterns
    const passwordPatterns = {
        length: /.{8,}/,
        lowercase: /[a-z]/,
        uppercase: /[A-Z]/,
        number: /[0-9]/
    };

    // Email validation pattern
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    // Dark mode functionality
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.classList.add(currentTheme);
    }

    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
    });

    // Prevent whitespace in inputs
    inputs.forEach(input => {
        input.addEventListener('input', (e) => {
            // Remove whitespace as user types
            if (input.type !== 'email') { // Allow spaces in email
                e.target.value = e.target.value.replace(/\s/g, '');
            }
        });

        input.addEventListener('blur', (e) => {
            // Trim whitespace on blur
            e.target.value = e.target.value.trim();
            
            // Validate email on blur
            if (input.type === 'email') {
                validateEmail(e.target.value);
            }
        });
    });

    // Email validation
    function validateEmail(email) {
        const isValid = emailPattern.test(email);
        emailInput.classList.toggle('valid', isValid);
        emailInput.classList.toggle('invalid', !isValid);

        if (!isValid && email.length > 0) {
            showError(emailInput, 'Please enter a valid email address');
        } else {
            clearError(emailInput);
        }

        return isValid;
    }

    // Password validation
    function validatePassword(password) {
        const checks = {
            length: passwordPatterns.length.test(password),
            lowercase: passwordPatterns.lowercase.test(password),
            uppercase: passwordPatterns.uppercase.test(password),
            number: passwordPatterns.number.test(password)
        };

        // Update requirement indicators
        document.getElementById('length-check').classList.toggle('valid', checks.length);
        document.getElementById('lowercase-check').classList.toggle('valid', checks.lowercase);
        document.getElementById('uppercase-check').classList.toggle('valid', checks.uppercase);
        document.getElementById('number-check').classList.toggle('valid', checks.number);

        // Update input styling
        passwordInput.classList.toggle('valid', Object.values(checks).every(Boolean));
        passwordInput.classList.toggle('invalid', !Object.values(checks).every(Boolean));

        return Object.values(checks).every(Boolean);
    }

    // Password visibility toggle
    const passwordToggles = document.querySelectorAll('.password-toggle');
    
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            const button = e.currentTarget;
            const passwordField = button.parentElement.querySelector('input');
            const eyeIcon = button.querySelector('.eye');
            const eyeOffIcon = button.querySelector('.eye-off');

            // Toggle password visibility
            const type = passwordField.type === 'password' ? 'text' : 'password';
            passwordField.type = type;

            // Toggle icons
            eyeIcon.classList.toggle('hidden');
            eyeOffIcon.classList.toggle('hidden');

            // Update aria-label
            button.setAttribute('aria-label', 
                type === 'password' ? 'Show password' : 'Hide password'
            );
        });
    });

    // Real-time validation
    passwordInput.addEventListener('input', (e) => {
        validatePassword(e.target.value);
    });

    emailInput.addEventListener('input', (e) => {
        validateEmail(e.target.value);
    });

    // Form submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        let isValid = true;
        
        // Check for empty fields
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                showError(input, 'This field is required');
            }
        });

        // Validate email
        if (!validateEmail(emailInput.value)) {
            isValid = false;
            if (!emailInput.value) {
                showError(emailInput, 'Email is required');
            }
        }

        // Validate password
        if (!validatePassword(passwordInput.value)) {
            isValid = false;
            if (!passwordInput.value) {
                showError(passwordInput, 'Password is required');
            } else {
                showError(passwordInput, 'Please meet all password requirements');
            }
        }

        // Validate name fields
        const firstNameInput = document.getElementById('firstname');
        const lastNameInput = document.getElementById('lastname');

        if (!firstNameInput.value.trim()) {
            isValid = false;
            showError(firstNameInput, 'First name is required');
        } else if (firstNameInput.value.length < 2) {
            isValid = false;
            showError(firstNameInput, 'First name must be at least 2 characters');
        } else {
            clearError(firstNameInput);
        }

        if (!lastNameInput.value.trim()) {
            isValid = false;
            showError(lastNameInput, 'Last name is required');
        } else if (lastNameInput.value.length < 2) {
            isValid = false;
            showError(lastNameInput, 'Last name must be at least 2 characters');
        } else {
            clearError(lastNameInput);
        }

        // If all validations pass, submit the form
        if (isValid) {
            form.submit();
        }
    });

    // Helper functions
    function showError(input, message) {
        const errorDiv = input.parentElement.querySelector('.error-message') || 
                        createErrorElement(input);
        errorDiv.textContent = message;
        errorDiv.classList.add('visible');
        input.classList.add('invalid');
    }

    function clearError(input) {
        const errorDiv = input.parentElement.querySelector('.error-message');
        if (errorDiv) {
            errorDiv.classList.remove('visible');
        }
        input.classList.remove('invalid');
    }

    function createErrorElement(input) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        input.parentElement.appendChild(errorDiv);
        return errorDiv;
    }
});
