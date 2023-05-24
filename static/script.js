// *********dark mode working code for single webpage*********
// Add event listener to the window object
window.addEventListener('DOMContentLoaded', () => {
    // Get the dark mode toggle button element
    const darkModeToggle = document.querySelector('#dark-mode-toggle');

    // Add event listener to the toggle button
    darkModeToggle.addEventListener('click', () => {
        // Toggle the dark mode class on the document body
        document.body.classList.toggle('dark-mode');
    });
});

// copy buttons
// copier for output i.e., Encryption
function copier() {
    const a = document.getElementById("output");
    a.select();
    navigator.clipboard.writeText(a.value);
}

// copier for output i.e., Encryption
function copier1() {
    const a = document.getElementById("output1");
    a.select();
    navigator.clipboard.writeText(a.value);
}