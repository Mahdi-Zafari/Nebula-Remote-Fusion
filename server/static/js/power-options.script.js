document.querySelectorAll('.power-option').forEach(button => {
    button.addEventListener('click', () => {
        const action = button.id;
        showLoading(action);

        $.ajax({
            url: `/${action}`,
            type: 'POST',
            success: function(response) {
                showMessage('success', `${action.charAt(0).toUpperCase() + action.slice(1)} was successful!`);
                setTimeout(() => {
                    window.location.href = '/operation_status';
                }, 1000);
            },
            error: function(xhr, status, error) {
                console.error(`Error: ${xhr.status} - ${error}`);
                showMessage('error', `An error occurred: ${xhr.responseText || error}`);
                hideLoading();
            }
        });
    });
});

function showLoading(action) {
    const loadingMessageSpan = document.querySelector('.loading-message span');
    if (loadingMessageSpan) {
        loadingMessageSpan.textContent = `Loading ${action.charAt(0).toUpperCase() + action.slice(1)}...`;
    }
    document.body.classList.add('loading-active');
}

function hideLoading() {
    document.body.classList.remove('loading-active');
}

function showMessage(type, message) {
    const successMessage = document.getElementById('success-message');
    const errorMessage = document.getElementById('error-message');

    if (type === 'success') {
        successMessage.textContent = message;
        successMessage.style.display = 'block';
        errorMessage.style.display = 'none';
    } else if (type === 'error') {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        successMessage.style.display = 'none';
    }

    setTimeout(() => {
        successMessage.style.display = 'none';
        errorMessage.style.display = 'none';
    }, 5000);
}
