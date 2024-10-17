function showMessageCC(message, type) {
    const messageElement = document.getElementById(`${type}-message`);
    messageElement.textContent = message;
    messageElement.style.display = 'block';

    setTimeout(() => {
        messageElement.style.display = 'none';
    }, 3000);
}

function updateBatteryIcon(percentage, plugged) {
    const batteryIcon = document.getElementById('battery-icon');
    batteryIcon.className = plugged ? 'bx bxs-battery-charging' : getBatteryIconClass(percentage);
}

function getBatteryIconClass(percentage) {
    if (percentage >= 80) return 'bx bxs-battery-full';
    if (percentage >= 50) return 'bx bxs-battery';
    if (percentage >= 20) return 'bx bxs-battery-low';
    return 'bx bxs-battery-empty';
}

function fetchAndUpdate(url, elementId, valueKey) {
    $.ajax({
        url: url,
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            const element = document.getElementById(elementId);
            if (data[valueKey] !== undefined) {
                element.innerText = data[valueKey] === 'on' ? 'On' : 'Off';
            } else {
                showMessageCC(`Invalid data format from ${url}`, 'error');
            }
        },
        error: function(xhr, status, error) {
            console.error(`Failed to fetch data from ${url}`, error);
            showMessageCC(`Failed to fetch data from ${url}`, 'error');
        }
    });
}

function getBatteryLevel() {
    $.ajax({
        url: '/battery',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            const batteryLevelSpan = document.querySelector('.control-device span');
            if (data.percentage !== undefined) {
                batteryLevelSpan.textContent = `${data.percentage}%`;
                updateBatteryIcon(data.percentage, data.plugged);
            } else {
                batteryLevelSpan.textContent = "Battery info not available";
                showMessageCC('Battery info not available', 'error');
            }
        },
        error: function(xhr, status, error) {
            console.error('Error fetching battery data:', error);
            showMessageCC('Error fetching battery data', 'error');
        }
    });
}

function updatePerformance(data) {
    document.getElementById('cpu-usage').textContent = `CPU: ${data.cpu_usage}%`;
    document.getElementById('ram-usage').textContent = `RAM: ${data.ram_usage}%`;
    document.getElementById('disk-usage').textContent = `Disk: ${data.disk_usage}%`;

    const uptime = new Date(data.uptime * 1000);
    document.getElementById('uptime').textContent = `Uptime: ${uptime.getUTCHours()}h ${uptime.getUTCMinutes()}m ${uptime.getUTCSeconds()}s`;
}

function getPerformanceData() {
    $.ajax({
        url: '/performance',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            updatePerformance(data);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching performance data:', error);
            showMessageCC('Error fetching performance data', 'error');
        }
    });
}

function updateStatus() {
    fetchAndUpdate('/wifi/status', 'wifi-status', 'wifi_status');
    fetchAndUpdate('/bluetooth/status', 'bluetooth-status', 'bluetooth_status');
    fetchAndUpdate('/airplane/status', 'airplane-status', 'airplane_mode');
}

function adjustBrightness(change) {
    $.ajax({
        url: '/brightness/status',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            const currentBrightness = data.brightness;
            const newBrightness = Math.min(Math.max(currentBrightness + change, 0), 100);

            $.ajax({
                url: `/brightness/set/${newBrightness}`,
                method: 'POST',
                success: function(data) {
                    document.getElementById('brightness-status').textContent = `${data.brightness}%`;
                    showMessageCC(`Brightness set to ${data.brightness}%`, 'success');
                },
                error: function(xhr, status, error) {
                    console.error('Error adjusting brightness:', error);
                    showMessageCC('Error adjusting brightness', 'error');
                }
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching current brightness:', error);
            showMessageCC('Error fetching current brightness', 'error');
        }
    });
}

function adjustVolume(change) {
    $.ajax({
        url: '/volume/status',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            const currentVolume = data.volume;
            const newVolume = Math.min(Math.max(currentVolume + change, 0), 100);

            $.ajax({
                url: `/volume/set/${newVolume}`,
                method: 'POST',
                success: function(data) {
                    document.getElementById('volume-status').textContent = `${data.volume}%`;
                    showMessageCC(`Volume set to ${data.volume}%`, 'success');
                },
                error: function(xhr, status, error) {
                    console.error('Error adjusting volume:', error);
                    showMessageCC('Error adjusting volume', 'error');
                }
            });
        },
        error: function(xhr, status, error) {
            console.error('Error fetching current volume:', error);
            showMessageCC('Error fetching current volume', 'error');
        }
    });
}

function getBrightnessLevel() {
    $.ajax({
        url: '/brightness/status',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            document.getElementById('brightness-status').textContent = `${data.brightness}%`;
        },
        error: function(xhr, status, error) {
            console.error('Error fetching brightness data:', error);
            showMessageCC('Error fetching brightness data', 'error');
        }
    });
}

function getVolumeLevel() {
    $.ajax({
        url: '/volume/status',
        method: 'GET',
        dataType: 'json',
        success: function(data) {
            document.getElementById('volume-status').textContent = `${data.volume}%`;
        },
        error: function(xhr, status, error) {
            console.error('Error fetching volume data:', error);
            showMessageCC('Error fetching volume data', 'error');
        }
    });
}

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

$(document).ready(function() {
    getBatteryLevel();
    updateStatus();
    getPerformanceData();

    getBrightnessLevel();
    getVolumeLevel();

    setInterval(getBatteryLevel, 10000);
    setInterval(updateStatus, 10000);
    setInterval(getPerformanceData, 10000);

    setInterval(getBrightnessLevel, 10000);
    setInterval(getVolumeLevel, 10000);
});
