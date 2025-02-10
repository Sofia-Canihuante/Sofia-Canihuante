document.addEventListener("DOMContentLoaded", function() {
    console.log("Portfolio Loaded!");

    // Example: Change color of header when clicked
    document.querySelector("header").addEventListener("click", function() {
        this.style.backgroundColor = this.style.backgroundColor === "rgb(0, 123, 255)" ? "#0056b3" : "#007bff";
    });

    // Example: Alert when clicking the resume download button
    document.querySelector(".btn").addEventListener("click", function() {
        alert("Downloading Resume...");
    });
});
