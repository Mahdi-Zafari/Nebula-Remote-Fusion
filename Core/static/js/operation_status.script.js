document.addEventListener("DOMContentLoaded", () => {
    const statusTitle = document.getElementById("status-title");
    const statusDescription = document.getElementById("status-description");
    const icon = document.querySelector(".icon-box i");

    function checkConnection() {
        statusTitle.textContent = "Checking connection...";
        statusDescription.textContent = "Please wait while we check the connection status.";
        icon.className = 'bx bx-loader-circle';

        fetch("/check-connection")
            .then(response => {
                if (response.ok) {
                    statusTitle.textContent = "Connection Established";
                    statusDescription.textContent = "Your connection is stable.";
                    icon.className = 'bx bx-check-circle success-icon';
                } else {
                    throw new Error('Connection lost');
                }
            })
            .catch(error => {
                statusTitle.textContent = "Connection Lost";
                statusDescription.textContent = "Please check your internet connection and try again.";
                icon.className = 'bx bx-error-circle error-icon';
            });
    }

    checkConnection();

    setInterval(checkConnection, 10000);
});
