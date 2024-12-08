import time
from PyQt6.QtCore import QThread, pyqtSignal
from pynput.keyboard import Key, Controller
from utils import load_special_buttons


class WorkerThread(QThread):
    status_signal = pyqtSignal(str)  # Signal for updating status messages

    def __init__(self, queue, times):
        super().__init__()
        self.queue = queue
        self.times = times
        self.keyboard = Controller()
        self.stop_flag = False
        self.specialbutton = load_special_buttons()

    def run(self):
        # Countdown before starting
        for i in range(3, 0, -1):
            self.status_signal.emit(f"Starting in: {i} seconds")
            time.sleep(1)
            if self.stop_flag:
                return

        if self.times > 0:  # Fixed number of repetitions
            for _ in range(self.times):
                if self.stop_flag:
                    break
                self.process_queue()
        else:  # Infinite loop
            while not self.stop_flag:
                self.process_queue()

    def process_queue(self):
        for i in range(len(self.queue)):
            if self.stop_flag:
                return

            key = self.queue[i]
            if (i + 1) % 2 != 0:  # Command (key press)
                self.status_signal.emit(f"Executing command: {key}")
                if key in self.specialbutton:
                    self.keyboard.press(self.specialbutton[key])
                    time.sleep(0.1)
                    self.keyboard.release(self.specialbutton[key])
                else:
                    self.keyboard.press(key)
                    time.sleep(0.1)
                    self.keyboard.release(key)
            else:  # Delay
                delay = int(self.queue[i])
                end_time = time.time() + delay
                while time.time() < end_time:
                    if self.stop_flag:
                        return
                    remaining = int(end_time - time.time())
                    self.status_signal.emit(f"Waiting: {remaining} seconds")
                    time.sleep(
