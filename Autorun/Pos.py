import pyautogui
import time
import sys

while True:
	x, y = pyautogui.position()
    
	sys.stdout.write(f"\r({x}, {y})  ")
    
	time.sleep(0.5)