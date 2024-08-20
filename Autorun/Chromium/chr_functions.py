import pyautogui
import time

# Página anterior
def chr_pag_anterior():
    pyautogui.hotkey('alt', 'left')
    time.sleep(10)
    
# Página siguiente
def chr_pag_siguiente():
    pyautogui.hotkey('alt', 'right')
    time.sleep(10)

# Cerrar pestaña
def chr_cerrar_pestana():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(4)

# Pestaña anterior
def chr_pestana_anterior():
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1)

# Pestaña siguiente
def chr_pestana_siguiente():
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(1)

# Recargar página
def chr_rec_pag():
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(15)

# Cerrar ventana de restaurar páginas
def chr_error_cerrar():
    pyautogui.moveTo(1008, 88)
    pyautogui.click()
    time.sleep(0.5)

# MultiLogin
def chr_multilogin():
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.moveTo(874, 54)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(710, 294)
    pyautogui.click()
    time.sleep(0.5)
