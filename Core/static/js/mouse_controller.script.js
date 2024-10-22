function moveMouse(direction) {
    let url = '';

    switch (direction) {
        case 'up':
            url = '/mouse/move/up';
            break;
        case 'down':
            url = '/mouse/move/down';
            break;
        case 'left':
            url = '/mouse/move/left';
            break;
        case 'right':
            url = '/mouse/move/right';
            break;
        default:
            console.error('Invalid mouse direction');
            return;
    }

    $.ajax({
        url: url,
        method: 'POST',
        success: function(response) {
            console.log(response.status);
            showMessageCC(response.status, 'success');
        },
        error: function(xhr, status, error) {
            console.error('Error moving mouse:', error);
            showMessageCC('Error moving mouse', 'error');
        }
    });
}

function mouseClick(button) {
    let url = '';

    switch (button) {
        case 'left':
            url = '/mouse/click/left';
            break;
        case 'right':
            url = '/mouse/click/right';
            break;
        default:
            console.error('Invalid mouse button');
            return;
    }

    $.ajax({
        url: url,
        method: 'POST',
        success: function(response) {
            console.log(response.status);
            showMessageCC(response.status, 'success');
        },
        error: function(xhr, status, error) {
            console.error('Error clicking mouse:', error);
            showMessageCC('Error clicking mouse', 'error');
        }
    });
}

function scrollMouse(direction) {
    let url = '';

    switch (direction) {
        case 'up':
            url = '/mouse/scroll/up';
            break;
        case 'down':
            url = '/mouse/scroll/down';
            break;
        default:
            console.error('Invalid scroll direction');
            return;
    }

    $.ajax({
        url: url,
        method: 'POST',
        success: function(response) {
            console.log(response.status);
            showMessageCC(response.status, 'success');
        },
        error: function(xhr, status, error) {
            console.error('Error scrolling:', error);
            showMessageCC('Error scrolling', 'error');
        }
    });
}

function showMessageCC(message, type) {
    const messageElement = document.getElementById(`${type}-message`);
    messageElement.textContent = message;
    messageElement.style.display = 'block';

    setTimeout(() => {
        messageElement.style.display = 'none';
    }, 3000);
}
