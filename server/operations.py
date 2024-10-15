from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from flask import jsonify
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import subprocess
import pyautogui
import comtypes
import psutil
import json
import os

config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')

if not os.path.isfile(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

with open(config_path, 'r') as config_file:
    config = json.load(config_file)

mouse_movement_x = config.get("mouse_movement", {}).get("x", 0)
mouse_movement_y = config.get("mouse_movement", {}).get("y", 0)

def register_routes(app):
    @app.route('/check-connection')
    def check_connection():
        return '', 200

    @app.route('/restart')
    def restart():
        try:
            os.system('shutdown /r /t 1')
            return "Restarting...", 200
        except Exception as e:
            return str(e), 700

    @app.route('/shutdown')
    def shutdown():
        try:
            os.system('shutdown /s /t 1')
            return "Shutting down...", 200
        except Exception as e:
            return str(e), 700

    @app.route('/sleep')
    def sleep():
        try:
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
            return "Going to sleep...", 200
        except Exception as e:
            return str(e), 700

    @app.route('/lock')
    def lock():
        try:
            os.system("rundll32.exe user32.dll,LockWorkStation")
            return "Locking...", 200
        except Exception as e:
            return str(e), 700

    @app.route('/battery')
    def battery():
        try:
            battery = psutil.sensors_battery()
            if battery:
                return jsonify({
                    'percentage': battery.percent,
                    'plugged': battery.power_plugged
                }), 200
            else:
                return "Battery information not available", 404
        except Exception as e:
            return str(e), 500

    @app.route('/wifi/status')
    def wifi_status():
        try:
            result = subprocess.check_output("netsh interface show interface", shell=True, text=True)
            if "Wi-Fi" in result and "Connected" in result:
                return jsonify({'wifi_status': 'on'}), 200
            else:
                return jsonify({'wifi_status': 'off'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/bluetooth/status')
    def bluetooth_status():
        try:
            result = subprocess.check_output("netsh interface show interface", shell=True, text=True)
            if "Bluetooth" in result and "Connected" in result:
                return jsonify({'bluetooth_status': 'on'}), 200
            else:
                return jsonify({'bluetooth_status': 'off'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/airplane/status')
    def airplane_status():
        try:
            result = subprocess.check_output("powershell -Command Get-NetAdapter", shell=True, text=True)
            if "Airplane" in result:
                return jsonify({'airplane_mode': 'on'}), 200
            else:
                return jsonify({'airplane_mode': 'off'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/brightness/set/<int:level>', methods=['POST'])
    def set_brightness(level):
        try:
            if 0 <= level <= 100:
                subprocess.Popen(f"powershell (Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})", shell=True)
                return jsonify({'brightness': level}), 200
            else:
                return "Brightness level must be between 0 and 100", 400
        except Exception as e:
            return str(e), 500

    @app.route('/brightness/status')
    def brightness_status():
        try:
            result = subprocess.check_output("powershell (Get-WmiObject -Namespace root/wmi -Class WmiMonitorBrightness).CurrentBrightness", shell=True, text=True)
            return jsonify({'brightness': int(result.strip())}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/volume/set/<int:level>', methods=['POST'])
    def set_volume(level):
        try:
            if 0 <= level <= 100:
                comtypes.CoInitialize()

                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                volume = cast(interface, POINTER(IAudioEndpointVolume))

                volume.SetMasterVolumeLevelScalar(level / 100, None)

                return jsonify({'volume': level}), 200
            else:
                return jsonify({'error': 'Volume level must be between 0 and 100'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            comtypes.CoUninitialize()

    @app.route('/volume/status')
    def volume_status():
        try:
            comtypes.CoInitialize()

            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))

            current_volume = volume.GetMasterVolumeLevelScalar() * 100

            return jsonify({'volume': int(current_volume)}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            comtypes.CoUninitialize()

    @app.route('/performance')
    def performance():
        try:
            cpu_usage = psutil.cpu_percent(interval=1)

            memory = psutil.virtual_memory()
            ram_usage = memory.percent

            disk = psutil.disk_usage('/')
            disk_usage = disk.percent

            uptime = psutil.boot_time()

            return jsonify({
                'cpu_usage': cpu_usage,
                'ram_usage': ram_usage,
                'disk_usage': disk_usage,
                'uptime': uptime
            }), 200
        except Exception as e:
            return str(e), 500

    @app.route('/mouse/move/up', methods=['POST'])
    def move_mouse_up():
        try:
            current_position = pyautogui.position()
            pyautogui.moveTo(current_position.x, current_position.y - mouse_movement_y)
            return jsonify({'status': 'mouse moved up'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/mouse/move/down', methods=['POST'])
    def move_mouse_down():
        try:
            current_position = pyautogui.position()
            pyautogui.moveTo(current_position.x, current_position.y + mouse_movement_y)
            return jsonify({'status': 'mouse moved down'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/mouse/move/left', methods=['POST'])
    def move_mouse_left():
        try:
            current_position = pyautogui.position()
            pyautogui.moveTo(current_position.x - mouse_movement_x, current_position.y)
            return jsonify({'status': 'mouse moved left'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/mouse/move/right', methods=['POST'])
    def move_mouse_right():
        try:
            current_position = pyautogui.position()
            pyautogui.moveTo(current_position.x + mouse_movement_x, current_position.y)
            return jsonify({'status': 'mouse moved right'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
