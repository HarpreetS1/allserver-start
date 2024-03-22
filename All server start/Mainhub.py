import webbrowser
import pyautogui
import time

def open_chrome_incognito(urlHub):
    # Open Chrome
    webbrowser.open_new_tab("https://www.google.com")
    time.sleep(2)  # Wait for Chrome to open
    # Bring Chrome window to foreground (optional)
    #pyautogui.hotkey('alt', 'tab')
    #time.sleep(0.5)
    # Open incognito mode
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(6)  # Wait for incognito mode to activate
    # Open URL
    pyautogui.typewrite(urlHub)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for the page to load
    
    pyautogui.click(x=616, y=392) 
    pyautogui.typewrite("NOOBMASTER3")
    pyautogui.click(x=622, y=465)
    pyautogui.typewrite("happyishappy")
    pyautogui.press('enter')
    time.sleep(10)  # Wait for the action to take effect
    # Example: Clicking at a specific position
    pyautogui.click(x=349, y=232)  # Adjust the coordinates as needed
    time.sleep(10)
    pyautogui.click(x=1024, y=260)
    time.sleep(10)
    pyautogui.click(x=1339, y=15) 

if __name__ == "__main__":
    urlHub = "https://panel.magmanode.com/auth/login"
    open_chrome_incognito(urlHub)