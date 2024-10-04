document.querySelectorAll('.power-option').forEach(button => {
    button.addEventListener('click', () => {
        const action = button.id;
        showLoading(action);

        fetch(`/${action}`)
            .then(response => {
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Error: ' + response.status);
                }
            })
            .then(() => {
                showMessage('success', 'Operation was successful!');

                setTimeout(() => {
                    window.location.href = '/operation_status';
                }, 1000);
            })
            .catch(error => {
                console.error(error);
                showMessage('error', 'An error occurred: ' + error.message);
                hideLoading();
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
        if (successMessage) {
            successMessage.textContent = message;
            successMessage.style.display = 'block';
        }
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }
    } else if (type === 'error') {
        if (errorMessage) {
            errorMessage.textContent = message;
            errorMessage.style.display = 'block';
        }
        if (successMessage) {
            successMessage.style.display = 'none';
        }
    }

    setTimeout(() => {
        if (successMessage) {
            successMessage.style.display = 'none';
        }
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }
    }, 5000);
}
