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

ins_dif_seguidores_bot = 0

# Calcular diferencia de seguidores del bot (iteración máxima)
def ins_calc_dif_seg_bot():
    global ins_dif_seguidores_bot
    
    ins_dif_seguidores_bot = ins_num_seguidores_bot - ins_num_seguidores_bot_prev
    
    if ins_dif_seguidores_bot < 5:
        ins_dif_seguidores_bot = 15

# Actualizar "seguidos" y "seguidores" del seguidor del bot
def ins_act_seg_seguidor():
    global ins_num_seguidos_seguidor, ins_num_seguidores_seguidor
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(ins_ffl_box)
    
    ins_num_seguidos_seguidor = gen_functions.gen_cifra(tmp_img, "Following")
    ins_num_seguidores_seguidor = gen_functions.gen_cifra(tmp_img, "Followers")

# Coordenas del botón "Follow", "Following", "Follow Back" de ventana de seguidores y seguidos
ins_bot_seg_box = [648, 186, 94, 22]

# Ajustar botón "Follow", "Following", "Follow back" de ventana de seguidores y seguidos
def ins_aj_seg_box():
    global ins_bot_seg_box
    
    # Desplazar verticalmente caja de captura de imagen para el botón
    ins_bot_seg_box[1] = gen_functions.gen_centro_xy[1]
    
    # Calcular centro del botón y retornar coordenadas
    return gen_functions.gen_calc_cent_rtn(ins_bot_seg_box)

# Evaluar si una palabra está presente
def ins_bl_pal(pal_ref):
    # Capturar área de la pantalla con el botón
    tmp_img = gen_functions.gen_capt_spec_pant(ins_bot_seg_box)
    
    # Obtener texto de la imagen
    tmp_txt = gen_functions.gen_text_img(tmp_img)
    
    # Evaluar si la palabra está presente en la imagen
    if tmp_txt == pal_ref:
        return True
    else:
        return False

# Actualizar fecha en txt
def ins_act_fecha():
    # Obtener fecha y hora de sesión previa
    fecha_prev = gen_functions.gen_busq_txt('Autorun/Instagram/Refs/ins_ref.txt', 0)
    
    # Obtener diferencia de horas entre fecha previa y actual
    dif_hr = gen_functions.gen_dif_hr(fecha_prev)
    
    # Si han pasado por lo menos 36 horas desde la última limpieza
    if dif_hr >= 36:
        # Actualizar fecha en txt
        gen_functions.gen_act_fecha('Autorun/Instagram/Refs/ins_ref.txt', 0)

# Actualizar número de seguidores del bot en txt
def ins_act_seg_txt():
    gen_functions.gen_act_txt('Autorun/Instagram/Refs/ins_ref.txt', 1, ins_num_seguidores_bot)



# 



def ins_ciclo_bot(val_seg, val_tiempo):
    # Abrir Instagram
    sys_functions.sys_abrir_tt()
    
    # Cerrar ventana de restaurar páginas
    chr_functions.chr_error_cerrar()
    
    # Ir a perfil de Instagram del bot
    ins_perfil_bot()
    
    # Obtener número de seguidos, seguidores y seguidores de sesión previa, del bot
    ins_act_seg_bot()
    ins_act_seguidores_bot_prev()
    
    # Revisar tiempo desde ultima sesión,limpiar "seguidos" si aplica
    ins_limp_seguidos_bot()
    
    # Ir a seguidores del bot
    ins_seguidores_pos()
    
    # Elegir un seguidor del bot
    ins_elegir_seguidor_bot()
    
    # Ir a seguidores del seguidor
    ins_seguidores_pos()
    
    # Seguir seguidores del seguidor
    ins_ciclo_busqueda(val_seg)
    
    # Cerrar ventana
    sys_functions.sys_cerrar_ventana()
    
    # Actualizar registro de sesión cada 36 horas o más
    ins_act_fecha()
    
    # Actualizar número de seguidores
    ins_act_seg_txt()
    
    # Esperar hasta reanudar el ciclo
    time.sleep(val_tiempo)
