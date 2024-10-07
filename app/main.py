from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
from threading import Timer
import subprocess
import webbrowser
import getpass
import json
import sys
import os

from ui.app_ui import Ui_main

config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')

if not os.path.isfile(config_path):
    raise FileNotFoundError(f"Config file not found: {config_path}")

with open(config_path, 'r') as config_file:
    config = json.load(config_file)

# =====  main app  ===== #
class win_main(QMainWindow, Ui_main):
    def __init__(self):
        super(win_main, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(":/img/img/nebula-RF-logo.png"))
        self.setWindowTitle("Nebula Remote Fusion")

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setup_tray_icon()
        self.set_pc_name()
        self.load_config()

        self.draggable = False

        self.widget_nav_background.hide()

        self.widget_success_message.hide()
        self.widget_error_message.hide()

        self.is_active = False
        self.setup_buttons()

        self.config_timer = QTimer(self)
        self.config_timer.timeout.connect(self.load_config)
        self.config_timer.start(10000)

    def setup_tray_icon(self):
        """Setup system tray icon and its menu."""
        self.tray_icon = QSystemTrayIcon(QIcon(":/img/img/nebula-RF-logo.png"), parent=self)
        self.tray_icon.setToolTip("Nebula Remote Fusion")

        self.tray_menu = QMenu()
        quit_action = QAction("Quit", self)
        quit_action.triggered.connect(self.close_program)
        self.tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.activated.connect(self.tray_icon_clicked)

    def setup_buttons(self):
        """Setup button group and connect signals to slots."""
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.btn_home)
        self.button_group.addButton(self.btn_more)

        self.btn_home.setChecked(True)

        self.btn_home.clicked.connect(self.open_home_page)
        self.btn_more.clicked.connect(self.open_more_page)
        self.Button_exit.clicked.connect(self.close_program)
        self.Button_minimized.clicked.connect(self.minimize_to_tray)
        self.btn_open_nav_menu.clicked.connect(self.open_nav_menu)
        self.btn_close_nav_menu.clicked.connect(self.close_nav_menu)

        self.Btn_active_inactive.clicked.connect(self.toggle_status)
        self.btn_open_browser.clicked.connect(self.open_browser)

        self.btn_save_change_username_password.clicked.connect(self.save_username_password)
        self.btn_save_change_ip_port.clicked.connect(self.save_ip_port)

        self.checkBox_auto_open_browser.stateChanged.connect(self.update_auto_open_browser)
        self.checkBox_cache_logging.stateChanged.connect(self.update_cache_logging)

    def load_config(self):
        """Load configuration from JSON file."""
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')
        server_config_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'config', 'main.config.json')
        server_config_path = os.path.abspath(server_config_path)

        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r') as config_file:
            self.config = json.load(config_file)

        with open(server_config_path, 'r') as config_file:
            server_config = json.load(config_file)

        self.ip_v_input.setText(self.config['server']['host'])
        self.port_v_input.setText(str(self.config['server']['port']))

        self.ip_ch_input.setText(self.config['server']['host'])
        self.port_ch_input.setText(str(self.config['server']['port']))

        self.checkBox_auto_open_browser.setChecked(self.config.get('open_browser', False))

        self.checkBox_cache_logging.setChecked(server_config.get('save_tokens', False))

    def set_pc_name(self):
        """Set the current PC user name to label_pcname."""
        user_name = getpass.getuser()
        if len(user_name) > 11:
            user_name = user_name[:11] + "..."
        self.label_pcname.setText(user_name)

    def save_username_password(self):
        """Save the username and password to the server config file."""

        username = self.username_ch_input.text()
        password = self.password_ch_input.text()

        if not username or not password:
            self.show_error_message("cannot be empty.")
            return

        try:
            server_config_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'config', 'main.config.json')
            server_config_path = os.path.abspath(server_config_path)

            with open(server_config_path, 'r') as config_file:
                server_config = json.load(config_file)

            server_config['user']['username'] = username
            server_config['user']['password'] = password

            with open(server_config_path, 'w') as config_file:
                json.dump(server_config, config_file, indent=4)

            self.show_success_message("updated successfully.")

        except Exception as e:
            self.show_error_message(f"Failed to update config: {str(e)}")

    def save_ip_port(self):
        """Save the IP and Port to the main config file."""

        ip = self.ip_ch_input.text()
        port = self.port_ch_input.text()

        if not ip or not port:
            self.show_error_message("cannot be empty.")
            return

        if not port.isdigit() or not (1 <= int(port) <= 65535):
            self.show_error_message("Invalid Port number.")
            return

        try:
            config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')

            if not os.path.isfile(config_path):
                raise FileNotFoundError(f"Config file not found: {config_path}")

            with open(config_path, 'r') as config_file:
                config = json.load(config_file)

            config['server']['host'] = ip
            config['server']['port'] = int(port)

            with open(config_path, 'w') as config_file:
                json.dump(config, config_file, indent=4)

            self.show_success_message("updated successfully.")

        except Exception as e:
            self.show_error_message(f"Failed to update config: {str(e)}")

    def update_auto_open_browser(self):
        """Update the auto-open browser setting in the config file."""
        auto_open = self.checkBox_auto_open_browser.isChecked()
        self.config['open_browser'] = auto_open
    
        config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')
    
        try:
            with open(config_path, 'w') as config_file:
                json.dump(self.config, config_file, indent=4)
    
            message = "Auto-open browser enabled." if auto_open else "Auto-open browser disabled."
            self.show_success_message(message)
    
        except Exception as e:
            self.show_error_message(f"Failed to update auto-open browser setting: {str(e)}")

    def update_cache_logging(self):
        """Update the cache logging setting in the server config file."""
        cache_logging = self.checkBox_cache_logging.isChecked()
        server_config_path = os.path.join(os.path.dirname(__file__), '..', 'server', 'config', 'main.config.json')

        try:
            with open(server_config_path, 'r') as config_file:
                server_config = json.load(config_file)

            server_config['save_tokens'] = cache_logging

            with open(server_config_path, 'w') as config_file:
                json.dump(server_config, config_file, indent=4)

            message = "Cache logging enabled." if cache_logging else "Cache logging disabled."
            self.show_success_message(message)

        except Exception as e:
            self.show_error_message(f"Failed to update cache logging setting: {str(e)}")

    # ===== Status management ===== #
    def update_status(self):
        """Update the label_stats text based on the current status."""
        if self.is_active:
            self.label_stats.setText("Active")
            self.show_success_message("Server is Active.")
        else:
            self.label_stats.setText("Inactive")
            self.show_error_message("Server is Inactive.")

    def toggle_status(self):
        """Toggle the active/inactive status when button is clicked."""
        self.is_active = not self.is_active
        self.update_status()

        if self.is_active:
            self.start_server()
        else:
            self.stop_server()

    def start_server(self):
        """Start the server using subprocess and open browser if configured."""
        try:
            self.server_process = subprocess.Popen(
                ["python", "server/app.py", "--host", self.config['server']['host'], "--port", str(self.config['server']['port'])]
            )
    
            if self.config.get('open_browser', True):
                def open_browser():
                    webbrowser.open(f"http://{self.config['server']['host']}:{self.config['server']['port']}")
                Timer(1, open_browser).start()
                print("Server started and browser opened.")
            else:
                print("Server started without opening the browser.")

            self.show_success_message("Server started successfully.")
        except Exception as e:
            self.show_error_message(f"Failed to start server: {str(e)}")

    def stop_server(self):
        """Stop the server process."""
        try:
            if hasattr(self, 'server_process') and self.server_process:
                self.server_process.terminate()
                self.server_process = None
                print("Server stopped.")
                self.show_success_message("Server stopped successfully.")
        except Exception as e:
            self.show_error_message(f"Failed to stop server: {str(e)}")

    def open_browser(self):
        """Open the browser with the server URL if active."""
        if not self.is_active:
            self.show_error_message("Please activate the server.")
            return
        
        try:
            ip = self.ip_v_input.text()
            port = self.port_v_input.text()

            url = f"http://{ip}:{port}"

            webbrowser.open(url)

            self.show_success_message("Browser opened successfully.")
        except Exception as e:
            self.show_error_message(f"Failed to open browser: {str(e)}")

    # ===== Window movement functionality ===== #
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.pos() in self.widget_top.rect():
            self.draggable = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


    # ===== System tray functionality ===== #
    def minimize_to_tray(self):
        """Minimize window to system tray."""
        self.hide()
        self.tray_icon.show()

    def tray_icon_clicked(self, reason):
        """Restore window when tray icon is clicked."""
        if reason == QSystemTrayIcon.Trigger:
            self.show_normal_window()

    def show_normal_window(self):
        """Restore window from system tray."""
        self.showNormal()
        self.tray_icon.hide()

    # ===== UI interactions ===== #
    def close_program(self):
        """Close the application."""
        if hasattr(self, 'server_process') and self.server_process is not None:
            self.stop_server()
        self.close()

    def open_nav_menu(self):
        """Open navigation menu."""
        self.widget_nav_background.show()

    def close_nav_menu(self):
        """Close navigation menu."""
        self.widget_nav_background.hide()

    def open_home_page(self):
        """Display the home page."""
        self.widget_home.show()
        self.widget_more.hide()
        self.widget_nav_background.hide()

    def open_more_page(self):
        """Display the more options page."""
        self.widget_home.hide()
        self.widget_more.show()
        self.widget_nav_background.hide()

    def show_success_message(self, message_text):
        """Show success message with the given text."""
        self.label_text_s_message.setText(message_text)
        self.widget_success_message.show()

        self.success_message_timer = QTimer(self)
        self.success_message_timer.setSingleShot(True)
        self.success_message_timer.timeout.connect(self.widget_success_message.hide)
        self.success_message_timer.start(3000)

    def show_error_message(self, message_text):
        """Show error message with the given text."""
        self.label_text_e_message.setText(message_text)
        self.widget_error_message.show()

        self.error_message_timer = QTimer(self)
        self.error_message_timer.setSingleShot(True)
        self.error_message_timer.timeout.connect(self.widget_error_message.hide)
        self.error_message_timer.start(3000)

def load_config():
    """Load configuration from JSON file."""
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'main.config.json')

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def run_server_in_background(host, port):
    """Run the server as a background process (invisible in Task Manager)."""
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        subprocess.Popen(
            ["python", "server/app.py", "--host", host, "--port", str(port)],
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
    except Exception as e:
        print(f"Failed to start server in background: {str(e)}")
        sys.exit(1)

def main():
    config = load_config()

    if config.get('gost', False):
        run_server_in_background(config['server']['host'], config['server']['port'])
    else:
        from PyQt5.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = win_main()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()
