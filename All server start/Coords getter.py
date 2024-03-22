import pyautogui
import time

def get_mouse_coordinates():
    print("Move your mouse to the desired location and click...")
    time.sleep(5)  # Delay to give user time to move mouse
    x, y = pyautogui.position()
    print(f"Coordinates: X={x}, Y={y}")

if __name__ == "__main__":
    get_mouse_coordinates()
