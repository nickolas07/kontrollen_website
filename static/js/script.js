function submitForm(identifier) {
    const dropdown = document.getElementById(`dropdown_${identifier}`);
    setTimeout(function() {
        dropdown.classList.remove('disabled');
        dropdown.classList.remove('btn-outline-secondary');
        dropdown.classList.add('btn-secondary');
    }, 2000); // 2000 milliseconds (2 seconds) delay
    return true;
}
    
function dark() {
    const toggleThemeInput = document.querySelector('.form-check-input');
    const toggleThemeLabel = document.querySelector('.form-check-label');
    const htmlTag = document.documentElement;

    htmlTag.setAttribute('data-bs-theme', 'dark');

    toggleThemeInput.id = 'flexSwitchCheckChecked';
    toggleThemeInput.setAttribute('checked', '');

    toggleThemeLabel.setAttribute('for', 'flexSwitchCheckChecked');
}

function light() {
    const toggleThemeInput = document.querySelector('.form-check-input');
    const toggleThemeLabel = document.querySelector('.form-check-label');
    const htmlTag = document.documentElement;

    htmlTag.setAttribute('data-bs-theme', 'light');

    toggleThemeInput.id = 'flexSwitchCheckDefault';
    toggleThemeInput.removeAttribute('checked');

    toggleThemeLabel.setAttribute('for', 'flexSwitchCheckDefault');
}


function getTheme() {
    let htmlTag = document.documentElement;
    return htmlTag.getAttribute('data-bs-theme');
}


function toggleTheme() {
    if (getTheme() === 'dark') {
        light();
    } else {
        dark();
    }
    localStorage.setItem('theme', getTheme());
}


function setTheme(theme) {
    if (theme === 'dark') {
        dark();
    } else {
        light();
    }
}

function focusNext(current) {
    const maxLength = 1;
    const currentLength = current.value.length;
    let next = current.nextElementSibling;
    current.setAttribute('maxLength', '1');

    if (currentLength >= 9 && next.value !== null) {
        let uuid = current.value;
        current.value = uuid.charAt(0);

        for (let i = 1; i <= 8; i++) {
            next.value = uuid.charAt(i);
            next = next.nextElementSibling;
        }
    }

    if (currentLength >= maxLength && next.value !== null) {
        next.setAttribute('maxLength', '1');

        while (next) {
            if (next.tagName.toLowerCase() === "input") {
                next.focus();
                break;
            }
            next = next.nextElementSibling;
        }
    }
}

