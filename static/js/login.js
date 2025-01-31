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

document.addEventListener('DOMContentLoaded', () => {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const togglePassword = document.getElementById('togglePassword');
    const password = document.getElementById('password');
    const loginForm = document.getElementById('loginForm');
    const languageSelect = document.getElementById('languageSelect');

    // Dark mode toggle
    darkModeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
    });

    // Password visibility toggle
    const passwordToggles = document.querySelectorAll('.password-toggle');
    
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            const button = e.currentTarget;
            const passwordField = button.parentElement.querySelector('input');
            const eyeIcon = button.querySelector('.eye');
            const eyeOffIcon = button.querySelector('.eye-off');

            // Toggle password visibility with smooth transition
            const type = passwordField.type === 'password' ? 'text' : 'password';
            passwordField.type = type;

            // Animate icon transition
            eyeIcon.classList.toggle('hidden');
            eyeOffIcon.classList.toggle('hidden');

            // Add ripple effect
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            button.appendChild(ripple);
            
            // Remove ripple after animation
            setTimeout(() => ripple.remove(), 1000);

            // Update aria-label for accessibility
            button.setAttribute('aria-label', 
                type === 'password' ? 'Show password' : 'Hide password'
            );
        });

        // Add hover animation pause
        toggle.addEventListener('mouseenter', () => {
            const eyeIcon = toggle.querySelector('.eye');
            eyeIcon.style.animationPlayState = 'running';
        });

        toggle.addEventListener('mouseleave', () => {
            const eyeIcon = toggle.querySelector('.eye');
            eyeIcon.style.animationPlayState = 'paused';
        });
    });

    // Original password toggle (can be removed if only using the new one)
    togglePassword.addEventListener('click', () => {
        const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
        password.setAttribute('type', type);
        togglePassword.classList.toggle('show');
    });


    // Form submission (prevent default for demo)
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        console.log('Form submitted');
    });

    // Language selection (demo - you would typically use a translation library)
    languageSelect.addEventListener('change', (e) => {
        console.log(`Language changed to: ${e.target.value}`);
    });

    // Subtle hover animation for buttons and links
    const interactiveElements = document.querySelectorAll('button, a');
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
