const tabToggles = document.querySelectorAll('.tabToggle');
const tabContents = document.querySelectorAll('.tabcontent');

tabToggles.forEach((toggle) => {
    toggle.addEventListener('click', () => {
        const tabId = toggle.getAttribute('data-tab');
        
        tabContents.forEach((content) => {
            content.style.display = 'none';
        });

        document.getElementById(tabId).style.display = 'block';
    });
});