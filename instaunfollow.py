import time
import ctypes


# Function to simulate a key press
def press_key(key):
    ctypes.windll.user32.keybd_event(key, 0, 0, 0)
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(key, 0, 2, 0)


# Key codes (Virtual-Key Codes): https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
VK_TAB = 0x09
VK_SPACE = 0x20

START_AFTER = 3  # seconds to wait before starting
TIME_GAP = 0.5  # seconds to wait between each key press
RESTART_AFTER = 1  # seconds to wait after each iteration
RUN_FOR = 100  # number of iterations

# Simulate pressing 'Tab' twice and 'Space' for 10 iterations
time.sleep(3)
for _ in range(RUN_FOR):
    press_key(VK_TAB)
    print("tab 1 pressed")
    time.sleep(TIME_GAP)
    press_key(VK_TAB)
    print("tab 2 pressed")
    time.sleep(TIME_GAP)
    press_key(VK_SPACE)
    print("space pressed")
    time.sleep(RESTART_AFTER)
