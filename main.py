from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QSpinBox, QFileDialog
from PyQt6.QtCore import Qt
from pynput import keyboard
from worker import WorkerThread
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minimal Keyboard Automation")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)  # Always on top

        layout = QVBoxLayout()

        self.label1 = QLabel("Enter commands (e.g., a,1,b,2):")
        layout.addWidget(self.label1)

        self.command_input = QLineEdit()
        layout.addWidget(self.command_input)

        self.load_button = QPushButton("Load Commands from File")
        self.load_button.clicked.connect(self.load_commands_from_file)
        layout.addWidget(self.load_button)

        self.save_button = QPushButton("Save Commands to File")
        self.save_button.clicked.connect(self.save_commands_to_file)
        layout.addWidget(self.save_button)

        self.label2 = QLabel("Number of repetitions (-1 for infinite):")
        layout.addWidget(self.label2)

        self.repeat_input = QSpinBox()
        self.repeat_input.setRange(-1, 1000)
        self.repeat_input.setValue(1)
        layout.addWidget(self.repeat_input)

        self.status_label = QLabel("Status: Waiting...")
        layout.addWidget(self.status_label)

        self.action_button = QPushButton("Start/Stop")
        self.action_button.clicked.connect(self.handle_action)
        layout.addWidget(self.action_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.thread = None

        # Start the shortcut listener
        self.shortcut_listener = keyboard.Listener(on_press=self.on_key_press)
        self.shortcut_listener.start()

    def handle_action(self):
        if self.thread is None or not self.thread.isRunning():
            self.start_process()
        else:
            self.stop_process()

    def start_process(self):
        queue = self.command_input.text().split(",")
        times = self.repeat_input.value()

        self.thread = WorkerThread(queue, times)
        self.thread.status_signal.connect(self.update_status)
        self.thread.start()
        self.action_button.setText("Stop")

    def stop_process(self):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()
        self.action_button.setText("Start")

    def update_status(self, message):
        self.status_label.setText(f"Status: {message}")

    def load_commands_from_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Select Command File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'r') as file:
                commands = file.read().strip()
                self.command_input.setText(commands)

    def save_commands_to_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getSaveFileName(self, "Save Command File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, 'w') as file:
                commands = self.command_input.text().strip()
                file.write(commands)

    def closeEvent(self, event):
        if self.thread and self.thread.isRunning():
            self.thread.stop()
            self.thread.wait()
        self.shortcut_listener.stop()  # Stop the shortcut listener
        super().closeEvent(event)

    def on_key_press(self, key):
        """Shortcut key handler."""
        try:
            if key == keyboard.Key.f12:  # Shortcut key: F12
                self.handle_action()
        except AttributeError:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
