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
    fetch(url)
        .then(response => {
            if (!response.ok) throw new Error(`Failed to fetch data from ${url}`);
            return response.json();
        })
        .then(data => {
            const element = document.getElementById(elementId);
            if (data[valueKey] !== undefined) {
                element.innerText = data[valueKey] === 'on' ? 'On' : 'Off';
            } else {
                throw new Error(`Invalid data format from ${url}`);
            }
        })
        .catch(error => {
            console.error(error);
            showMessageCC(error.message, 'error');
        });
}

function getBatteryLevel() {
    fetch('/battery')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch battery level');
            return response.json();
        })
        .then(data => {
            const batteryLevelSpan = document.querySelector('.control-device span');
            if (data.percentage !== undefined) {
                batteryLevelSpan.textContent = `${data.percentage}%`;
                updateBatteryIcon(data.percentage, data.plugged);
            } else {
                batteryLevelSpan.textContent = "Battery info not available";
                showMessageCC('Battery info not available', 'error');
            }
        })
        .catch(error => {
            console.error('Error fetching battery data:', error);
            showMessageCC('Error fetching battery data', 'error');
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
    fetch('/performance')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch performance data');
            return response.json();
        })
        .then(data => {
            updatePerformance(data);
        })
        .catch(error => {
            console.error('Error fetching performance data:', error);
            showMessageCC('Error fetching performance data', 'error');
        });
}

function updateStatus() {
    fetchAndUpdate('/wifi/status', 'wifi-status', 'wifi_status');
    fetchAndUpdate('/bluetooth/status', 'bluetooth-status', 'bluetooth_status');
    fetchAndUpdate('/airplane/status', 'airplane-status', 'airplane_mode');
}

// brightness, volume
function adjustBrightness(change) {
    fetch('/brightness/status')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch brightness level');
            return response.json();
        })
        .then(data => {
            const currentBrightness = data.brightness;
            const newBrightness = Math.min(Math.max(currentBrightness + change, 0), 100);

            fetch(`/brightness/set/${newBrightness}`, {
                method: 'POST'
            })
            .then(response => {
                if (!response.ok) throw new Error('Failed to set brightness');
                return response.json();
            })
            .then(data => {
                document.getElementById('brightness-status').textContent = `${data.brightness}%`;
                showMessageCC(`Brightness set to ${data.brightness}%`, 'success');
            })
            .catch(error => {
                console.error('Error adjusting brightness:', error);
                showMessageCC('Error adjusting brightness', 'error');
            });
        })
        .catch(error => {
            console.error('Error fetching current brightness:', error);
            showMessageCC('Error fetching current brightness', 'error');
        });
}

function adjustVolume(change) {
    fetch('/volume/status')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch volume level');
            return response.json();
        })
        .then(data => {
            const currentVolume = data.volume;
            const newVolume = Math.min(Math.max(currentVolume + change, 0), 100);

            fetch(`/volume/set/${newVolume}`, {
                method: 'POST'
            })
            .then(response => {
                if (!response.ok) throw new Error('Failed to set volume');
                return response.json();
            })
            .then(data => {
                document.getElementById('volume-status').textContent = `${data.volume}%`;
                showMessageCC(`Volume set to ${data.volume}%`, 'success');
            })
            .catch(error => {
                console.error('Error adjusting volume:', error);
                showMessageCC('Error adjusting volume', 'error');
            });
        })
        .catch(error => {
            console.error('Error fetching current volume:', error);
            showMessageCC('Error fetching current volume', 'error');
        });
}

function getBrightnessLevel() {
    fetch('/brightness/status')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch brightness level');
            return response.json();
        })
        .then(data => {
            document.getElementById('brightness-status').textContent = `${data.brightness}%`;
        })
        .catch(error => {
            console.error('Error fetching brightness data:', error);
            showMessageCC('Error fetching brightness data', 'error');
        });
}

function getVolumeLevel() {
    fetch('/volume/status')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch volume level');
            return response.json();
        })
        .then(data => {
            document.getElementById('volume-status').textContent = `${data.volume}%`;
        })
        .catch(error => {
            console.error('Error fetching volume data:', error);
            showMessageCC('Error fetching volume data', 'error');
        });
}

document.addEventListener('DOMContentLoaded', function() {
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
