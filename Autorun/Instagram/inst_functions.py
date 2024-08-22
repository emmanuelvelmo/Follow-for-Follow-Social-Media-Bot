from Autorun.System import sys_functions
from Autorun.Generic import gen_functions
from Autorun.Chromium import chr_functions
import pyautogui
import time

# Perfil de Instagram
def ins_perfil_bot():
    pyautogui.moveTo(0, 0)
    pyautogui.click()
    time.sleep(10)

# "Seguidos" del bot y seguidores del bot
def ins_siguiendo_pos():
    pyautogui.moveTo(0, 0)
    pyautogui.click()
    time.sleep(10)

# "Seguidores" del bot y seguidores del seguidor del bot
def ins_seguidores_pos():
    pyautogui.moveTo(0, 0)
    pyautogui.click()
    time.sleep(10)

# Colocar cursor sobre "Followers"
def ins_seguidores_pos_cur():
    pyautogui.moveTo(0, 0)
    time.sleep(1)

# Cerrar ventana chica
def ins_cerrar_ventana_ch():
    pyautogui.moveTo(0, 0)
    pyautogui.click()
    time.sleep(1)

# Posición en ventana chica
def ins_pos_ventana_ch():
    pyautogui.moveTo(0, 0)
    time.sleep(0.25)

# Número de seguidos y seguidores del bot en sesión actual y previa
ins_num_seguidos_bot = 0
ins_num_seguidores_bot = 0
ins_num_seguidores_bot_prev = 0

# Obtener número de seguidores del bot de sesión previa
def ins_act_seguidores_bot_prev():
    global ins_num_seguidores_bot_prev
    
    # Obtener cifra desde archivo de texto y convertir a entero
    ins_num_seguidores_bot_prev = int(gen_functions.gen_busq_txt('Autorun/Instagram/Refs/ins_ref.txt', 1))

# Coordenas para "Followers", "Following" y "Likes" del bot y seguidores del bot
ins_ffl_box = [0, 0, 0, 0]

# Número de seguidos y seguidores del seguidor
ins_num_seguidos_seguidor = 0
ins_num_seguidores_seguidor = 0

# Actualizar "seguidos" y "seguidores" del bot
def ins_act_seg_bot():
    global ins_num_seguidos_bot, ins_num_seguidores_bot
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(ins_ffl_box)
    
    ins_num_seguidos_bot = gen_functions.gen_cifra(tmp_img, "Following")
    ins_num_seguidores_bot = gen_functions.gen_cifra(tmp_img, "Followers")

