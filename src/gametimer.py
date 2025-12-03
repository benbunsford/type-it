from threading import Timer
import threading
import readchar
import queue
import termios
import sys


class GameTimer(Timer):
    def __init__(self, interval, function, args):
        super().__init__(interval, function, args)
        self.interval = interval
        self.function = function
        self.starting_interval = interval

    def speed_up(self):
        if self.interval > (self.starting_interval * 0.5):
            self.interval -= (self.starting_interval * 0.05)

class KeyReader():
    def __init__(self, timeout):
        self.queue = queue.Queue(1)
        self.timeout = timeout

    def read_key(self):
        pressed_key = readchar.readkey()
        self.queue.put(pressed_key)

    def read_key_async(self):
        thread = threading.Thread(target=self.read_key, daemon=True)
        thread.start()
        pressed_key = ''
        try:
            pressed_key = self.queue.get(block=True, timeout=self.timeout)
        except Exception as e:
            print(e)
        return pressed_key


class TerminalManager:
    def __init__(self):
        pass

    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.original_settings = termios.tcgetattr(self.fd)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.original_settings)
        return None
