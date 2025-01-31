// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const togglePassword = document.getElementById('togglePassword');
//     const password = document.getElementById('password');
//     const loginForm = document.getElementById('loginForm');
//     const languageSelect = document.getElementById('languageSelect');

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//     });

//     // Password visibility toggle
//     togglePassword.addEventListener('click', () => {
//         const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//         password.setAttribute('type', type);
//         togglePassword.classList.toggle('show');
//     });

//     // Form submission (prevent default for demo)
//     loginForm.addEventListener('submit', (e) => {
//         e.preventDefault();
//         console.log('Form submitted');
//     });

//     // Language selection (demo - you would typically use a translation library)
//     languageSelect.addEventListener('change', (e) => {
//         console.log(`Language changed to: ${e.target.value}`);
//     });

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

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const togglePassword = document.getElementById('togglePassword');
//     const password = document.getElementById('password');
//     const loginForm = document.getElementById('loginForm');
//     const languageSelect = document.getElementById('languageSelect');

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
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

//     // Original password toggle (can be removed if only using the new one)
//     togglePassword.addEventListener('click', () => {
//         const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//         password.setAttribute('type', type);
//         togglePassword.classList.toggle('show');
//     });


//     // Form submission (prevent default for demo)
//     loginForm.addEventListener('submit', (e) => {
//         e.preventDefault();
//         console.log('Form submitted');
//     });

//     // Language selection (demo - you would typically use a translation library)
//     languageSelect.addEventListener('change', (e) => {
//         console.log(`Language changed to: ${e.target.value}`);
//     });

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

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const togglePassword = document.getElementById('togglePassword');
//     const password = document.getElementById('password');
//     const loginForm = document.getElementById('loginForm');
//     const languageSelect = document.getElementById('languageSelect');

//     // Dark mode toggle
//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//     });

//     // Password visibility toggle
//     const passwordToggles = document.querySelectorAll('.password-toggle');
    
//     passwordToggles.forEach(toggle => {
//         toggle.addEventListener('click', (e) => {
//             const button = e.currentTarget;
//             const passwordField = button.parentElement.querySelector('input');
//             const eyeIcon = button.querySelector('.eye');
//             const eyeOffIcon = button.querySelector('.eye-off');

//             // Toggle password visibility with smooth transition
//             const type = passwordField.type === 'password' ? 'text' : 'password';
//             passwordField.type = type;

//             // Animate icon transition
//             eyeIcon.classList.toggle('hidden');
//             eyeOffIcon.classList.toggle('hidden');

//             // Add ripple effect
//             const ripple = document.createElement('span');
//             ripple.classList.add('ripple');
//             button.appendChild(ripple);
            
//             // Remove ripple after animation
//             setTimeout(() => ripple.remove(), 1000);

//             // Update aria-label for accessibility
//             button.setAttribute('aria-label', 
//                 type === 'password' ? 'Show password' : 'Hide password'
//             );
//         });

//         // Add hover animation pause
//         toggle.addEventListener('mouseenter', () => {
//             const eyeIcon = toggle.querySelector('.eye');
//             eyeIcon.style.animationPlayState = 'running';
//         });

//         toggle.addEventListener('mouseleave', () => {
//             const eyeIcon = toggle.querySelector('.eye');
//             eyeIcon.style.animationPlayState = 'paused';
//         });
//     });

//     // Original password toggle (can be removed if only using the new one)
//     togglePassword.addEventListener('click', () => {
//         const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
//         password.setAttribute('type', type);
//         togglePassword.classList.toggle('show');
//     });


//     // Form submission (prevent default for demo)
//     loginForm.addEventListener('submit', (e) => {
//         e.preventDefault();
//         console.log('Form submitted');
//     });

//     // Language selection (demo - you would typically use a translation library)
//     languageSelect.addEventListener('change', (e) => {
//         console.log(`Language changed to: ${e.target.value}`);
//     });

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

// document.addEventListener('DOMContentLoaded', () => {
//     const darkModeToggle = document.getElementById('darkModeToggle');
//     const body = document.body;
//     const form = document.querySelector('.form__container');
//     const emailInput = document.querySelector('input[type="email"]');

//     // Email validation pattern
//     const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

//     // Dark mode functionality
//     const currentTheme = localStorage.getItem('theme');
//     if (currentTheme) {
//         body.classList.add(currentTheme);
//     }

//     darkModeToggle.addEventListener('click', () => {
//         body.classList.toggle('dark-mode');
//         localStorage.setItem('theme', body.classList.contains('dark-mode') ? 'dark-mode' : '');
//     });

//     // Email validation
//     function validateEmail(email) {
//         // Remove any whitespace from the email
//         email = email.replace(/\s/g, '');
//         emailInput.value = email; // Update input value without spaces
        
//         const isValid = emailPattern.test(email);
//         emailInput.classList.toggle('valid', isValid && email.length > 0);
//         emailInput.classList.toggle('invalid', !isValid && email.length > 0);

//         if (!isValid && email.length > 0) {
//             showError(emailInput, 'Please enter a valid email address');
//         } else {
//             clearError(emailInput);
//         }

//         return isValid;
//     }

//     // Real-time email validation
//     emailInput.addEventListener('input', (e) => {
//         validateEmail(e.target.value);
//     });

//     // Password visibility toggle
//     const passwordToggles = document.querySelectorAll('.password-toggle');
    
//     passwordToggles.forEach(toggle => {
//         toggle.addEventListener('click', (e) => {
//             const button = e.currentTarget;
//             const passwordField = button.parentElement.querySelector('input');
//             const eyeIcon = button.querySelector('.eye');
//             const eyeOffIcon = button.querySelector('.eye-off');

//             const type = passwordField.type === 'password' ? 'text' : 'password';
//             passwordField.type = type;

//             eyeIcon.classList.toggle('hidden');
//             eyeOffIcon.classList.toggle('hidden');

//             button.setAttribute('aria-label', 
//                 type === 'password' ? 'Show password' : 'Hide password'
//             );
//         });
//     });

//     // Form submission
//     form.addEventListener('submit', (e) => {
//         e.preventDefault();
        
//         let isValid = true;
//         const email = emailInput.value.trim();

//         // Validate email
//         if (!validateEmail(email)) {
//             isValid = false;
//             if (!email) {
//                 showError(emailInput, 'Email is required');
//             }
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

//     // Add subtle hover animations
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
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const form = document.querySelector('.form__container');
    const emailInput = document.querySelector('input[type="email"]');
    const passwordInput = document.getElementById('password');
    const passwordToggle = document.querySelector('.password-toggle');

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

    // Email validation
    function validateEmail(email) {
        // Remove any whitespace from the email
        email = email.replace(/\s/g, '');
        emailInput.value = email; // Update input value without spaces
        
        const isValid = emailPattern.test(email);
        emailInput.classList.toggle('valid', isValid && email.length > 0);
        emailInput.classList.toggle('invalid', !isValid && email.length > 0);

        if (!isValid && email.length > 0) {
            showError(emailInput, 'Please enter a valid email address');
        } else {
            clearError(emailInput);
        }

        return isValid;
    }

    // Real-time email validation
    emailInput.addEventListener('input', (e) => {
        validateEmail(e.target.value);
    });

    // Enhanced password visibility toggle
    if (passwordToggle && passwordInput) {
        const eyeIcon = passwordToggle.querySelector('.eye');
        const eyeOffIcon = passwordToggle.querySelector('.eye-off');

        passwordToggle.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent form submission
            
            // Toggle password visibility
            const type = passwordInput.type === 'password' ? 'text' : 'password';
            passwordInput.type = type;

            // Toggle icon visibility with smooth transition
            eyeIcon.classList.toggle('hidden');
            eyeOffIcon.classList.toggle('hidden');

            // Update aria-label for accessibility
            passwordToggle.setAttribute('aria-label', 
                type === 'password' ? 'Show password' : 'Hide password'
            );

            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            passwordToggle.appendChild(ripple);
            
            // Remove ripple after animation
            setTimeout(() => ripple.remove(), 1000);
        });

        // Add hover animation for eye icon
        passwordToggle.addEventListener('mouseenter', () => {
            if (!eyeIcon.classList.contains('hidden')) {
                eyeIcon.style.animation = 'blink 1s ease infinite';
            }
        });

        passwordToggle.addEventListener('mouseleave', () => {
            eyeIcon.style.animation = 'none';
        });
    }


    // Form submission
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        let isValid = true;
        const email = emailInput.value.trim();

        // Validate email
        if (!validateEmail(email)) {
            isValid = false;
            if (!email) {
                showError(emailInput, 'Email is required');
            }
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

    // Add subtle hover animations for interactive elements
    const interactiveElements = document.querySelectorAll('button:not(.password-toggle), a');
    interactiveElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            element.style.transform = 'translateY(-2px)';
            element.style.transition = 'transform 0.3s ease';
        });
        element.addEventListener('mouseleave', () => {
            element.style.transform = 'translateY(0)';
        });
    });
});
