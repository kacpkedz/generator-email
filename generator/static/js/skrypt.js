document.addEventListener("DOMContentLoaded", function() {
    var copyButton = document.getElementById("copyButton");
    var email = document.querySelector(".email").textContent;

    copyButton.addEventListener("click", function() {
        copyToClipboard(email);
    });

    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(function() {
            alert("Email został skopiowany do schowka!");
        }, function() {
            alert("Wystąpił błąd podczas kopiowania do schowka!");
        });
    }
});
