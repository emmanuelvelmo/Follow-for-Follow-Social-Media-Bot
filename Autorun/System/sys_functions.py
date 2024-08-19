import pyautogui
import time

# Cerrar ventana
def sys_cerrar_ventana():
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)

# Abrir Chromium
def sys_abrir_chr():
    # Abrir Chromium desde el menú de aplicaciones
    pyautogui.moveTo(16, 586)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(100, 440)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(270, 440)
    pyautogui.click()
    time.sleep(20)
    
    # Cerrar ventana
    sys_cerrar_ventana()
    
    # Abrir Chromium desde el menú de aplicaciones
    pyautogui.moveTo(16, 586)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(100, 440)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(300, 440)
    pyautogui.click()
    time.sleep(20)
    
    # Pantalla completa
    pyautogui.press('f11')
    time.sleep(1)

# Abrir Instagram
def sys_abrir_inst():
    pyautogui.moveTo(16, 586)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(100, 440)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(300, 494)
    pyautogui.click()
    time.sleep(30)
    pyautogui.press('f11')
    time.sleep(1)

# Abrir Facebook
def sys_abrir_fb():
    pyautogui.moveTo(16, 586)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(100, 440)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(300, 470)
    pyautogui.click()
    time.sleep(30)
    pyautogui.press('f11')
    time.sleep(1)

# Abrir TikTok
def sys_abrir_tt():
    pyautogui.moveTo(16, 586)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(100, 440)
    pyautogui.click()
    time.sleep(0.25)
    pyautogui.moveTo(300, 520)
    pyautogui.click()
    time.sleep(50)
    pyautogui.press('f11')
    time.sleep(1)