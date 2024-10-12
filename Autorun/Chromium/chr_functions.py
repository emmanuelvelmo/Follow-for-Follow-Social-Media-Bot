import pyautogui
import time

# Pantalla completa
def chr_pant_comp():
    pyautogui.press('f11')
    time.sleep(1)

# Página anterior
def chr_pag_anterior():
    pyautogui.hotkey('alt', 'left')
    time.sleep(10)
    
# Página siguiente
def chr_pag_siguiente():
    pyautogui.hotkey('alt', 'right')
    time.sleep(10)

# Nueva pestaña
def chr_nueva_pestana():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)

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

# Final de la página
def chr_fin_pag():
    pyautogui.press('end')
    time.sleep(2)
    
# ChatGPT
def chr_bm_gpt():
    pyautogui.moveTo(60, 20)
    pyautogui.click()
    time.sleep(15)

# Cookies Profile Switcher
def chr_co_prof_swt():
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.moveTo(874, 54)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(710, 294)
    pyautogui.click()
    time.sleep(0.5)

# Ir a un sitio web
def chr_sit_web(val_url,val_tiempo):
    chr_pant_comp()
    pyautogui.press('f6')
    pyautogui.typewrite(val_url)
    pyautogui.press('enter')
    chr_pant_comp()
    time.sleep(val_tiempo)
