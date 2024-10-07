from flask import Flask, render_template, request, redirect, jsonify, url_for, session
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime, timezone, timedelta
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import subprocess
import comtypes
import psutil
import json
import jwt
import os

app = Flask(__name__)
app.secret_key = b'\x9c\xcfw\x14N\xd8\xf4\xdf\xf6\xba\x87I\xaf\x83\xcc\x85\x98\x1b\xd2\xba\x84\x9b\xee'

config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')

if not os.path.isfile(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

with open(config_path, 'r') as config_file:
    config = json.load(config_file)
    
token_config_path = os.path.join(os.path.dirname(__file__), 'config', 'token.config.json')

if 'model' in config and config['model']:
    model_template_path = f'model/{config["model"]}'
else:
    model_template_path = None

def render_model_template(template_name):
    if model_template_path and os.path.exists(os.path.join(app.root_path, 'templates', model_template_path, f'{template_name}.html')):
        return render_template(f'{model_template_path}/{template_name}.html')
    else:
        return render_template('404.html')

def save_tokens(data):
    with open(token_config_path, 'w') as f:
        json.dump(data, f)

def load_tokens():
    try:
        with open(token_config_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"tokens": []}
    
from datetime import datetime, timezone

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == config["user"]["username"] and password == config["user"]["password"]:
            token = jwt.encode({
                'username': username,
                'exp': datetime.now(timezone.utc) + timedelta(hours=1)
            }, app.secret_key)

            user_data = {
                'token': token,
                'created_at': datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                'expires_at': (datetime.now(timezone.utc) + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S"),\
                'ip': request.remote_addr,
                'user_agent': request.headers.get('User-Agent'),
                'device': request.user_agent.platform
            }

            if config.get('save_tokens', False):
                tokens = load_tokens()
                tokens['tokens'].append(user_data)
                save_tokens(tokens)

            session['token'] = token

            return redirect(url_for('home'))
        else:
            return render_model_template('access_denied')
    
    return render_model_template('Auth/login')

@app.before_request
def check_login():
    allowed_routes = ['login', 'static']
    if request.endpoint not in allowed_routes:
        token = session.get('token')

        if not token:
            return redirect(url_for('login'))

        try:
            jwt.decode(token, app.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
        
@app.route('/logout')
def logout():
    session.pop('token', None)
    return redirect(url_for('login'))

@app.route('/')
def home():
    return render_model_template('index')

@app.route('/operation_status')
def operation_status():
    return render_model_template('operation_status')

@app.errorhandler(404)
def not_found_error(e):
    return render_model_template('404'), 404

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
