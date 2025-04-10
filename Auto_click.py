# import time
# import threading
# from pynput.mouse import Button, Controller
# from pynput.keyboard import Listener, KeyCode

# count = 0
# delay = 0.1
# button = Button.left
# start_stop_key = KeyCode(char='a')
# stop_key = KeyCode(char='b')

# class ClickMouse(threading.Thread):
#     def __init__(self, delay, button):
#         super(ClickMouse, self).__init__()
#         self.delay = delay
#         self.button = button
#         self.running = False
#         self.program_running = True

#     def start_clicking(self):
#         self.running = True

#     def stop_clicking(self):
#         self.running = False

#     def exit(self):
#         self.stop_clicking()
#         self.program_running = False

#     def run(self):
#         global count
#         while self.program_running:
#             while self.running:
#                 mouse.click(self.button)
#                 time.sleep(self.delay)
#                 count += 1
#             time.sleep(0.9)
#         print("Total clicks:", count)  # Print the total count when the run method ends

# mouse = Controller()
# click_thread = ClickMouse(delay, button)
# click_thread.start()

# def on_press(key):
#     if key == start_stop_key:
#         if click_thread.running:
#             click_thread.stop_clicking()
#         else:
#             click_thread.start_clicking()

#     elif key == stop_key:
#         click_thread.exit()
#         listener.stop()

# with Listener(on_press=on_press) as listener:
#     listener.join()

# input('')








import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.00000000001
button = Button.left
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.count = 0  # Track click count within the class

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        mouse = Controller()
        while self.program_running:
            if self.running:
                mouse.click(self.button)
                self.count += 1
                time.sleep(self.delay)
            else:
                time.sleep(0.01)  # Short sleep while not running to avoid high CPU usage
        print("Total clicks:", self.count)  # Print click count when the thread exits

click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    elif key == stop_key:
        click_thread.exit()
        return False  # Stop listener

with Listener(on_press=on_press) as listener:
    listener.join()
input('')