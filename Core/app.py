from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timezone, timedelta
from operations import register_routes
import json
import jwt
import os

# //

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

@app.route('/mouse_controller')
def mouse_controller():
    return render_model_template('system_management/mouse_controller')

@app.route('/task_manager')
def task_manager():
    return render_model_template('system_management/task_manager')

@app.route('/remote_file_management')
def task_maremote_file_managementnager():
    return render_model_template('system_management/remote_file_management')

@app.route('/remote_command_prompt')
def remote_command_prompt():
    return render_model_template('system_management/remote_command_prompt')

@app.errorhandler(404)
def not_found_error(e):
    return render_model_template('404'), 404

register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
