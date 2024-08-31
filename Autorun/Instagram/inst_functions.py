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

# Cerrar pop up
def ins_cerrar_pop_up():
    pyautogui.moveTo(0, 0)
    pyautogui.click()
    time.sleep(1)

# Posición en pop up
def ins_pos_pop_up():
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

# Evaluar si una palabra está presente en el botón
def ins_bl_btn(pal_ref):
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

# Elegir a un seguidor del bot
def ins_elegir_seguidor_bot():
    # Calcular máximo de iteraciones
    ins_calc_dif_seg_bot()
    
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Iteraciones entre seguidores del bot
    for iter_seg in range(ins_dif_seguidores_bot):
        # Desplazar hacia abajo después del primer seguidor
        if bl_prim_usr:
            # Colocar cursor para desplazar hacia abajo
            ins_pos_pop_up()
            
            # Desplazar hacia el siguiente seguidor
            gen_functions.gen_desp_usr(ins_seg_box)
        
        # Encontrar nombre del seguidor y asignar coordenas
        gen_functions.gen_prim_usr(ins_seg_box)

        # Ajustar coordenadas de captura de popover


        # Evaluar si los seguidores son privados desde el popover


        # Si la cuenta no es privada
        if x:
            # Obtener número de "seguidos" y "seguidores" del seguidor desde el popover
            ins_act_seg_seguidor()
        
            # Calcular ratio del seguidor
            tmp_ratio = gen_functions.gen_act_ratio(ins_num_seguidos_seguidor, ins_num_seguidores_seguidor)
        
            # Si el ratio es igual o mayor al aceptado, cumple el mínimo de "seguidos"
            if tmp_ratio >= ins_ratio_min and ins_num_seguidos_seguidor >= ins_sig_min:
                # Ir a perfil del seguidor en nueva pestaña
                gen_functions.gen_ab_click_spec(25)

                # Cerrar pestaña anterior
                chr_functions.chr_pestana_anterior()
                chr_functions.chr_cerrar_pestana()
                
                break
        
        # Cambiar bool
        bl_prim_usr = True

# Ciclo de búsqueda
def ins_ciclo_busqueda(val_busq):
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Contador de seguidos
    cont_seg = 0
    
    # Iteraciones entre seguidores del seguidor
    for iter_seg in range(tt_num_seguidores_seguidor):
        if cont_seg == val_busq:
            break
        else:
            # Desplazar hacia abajo después del primer seguidor
            if bl_prim_usr:
                # Colocar cursor para desplazar hacia abajo
                tt_pos_pop_up()
                
                # Desplazar hacia el siguiente seguidor
                gen_functions.gen_desp_usr(tt_seg_box)
            
            # Encontrar nombre del seguidor y asignar coordenas a variable genérica
            gen_functions.gen_prim_usr(tt_seg_box)
            
            # Asignar coordenas del centro del botón
            coords_btn = tt_aj_seg_box()
            
            # Evaluar si la palabra "Follow" está presente
            bl_follow = tt_bl_pal("Follow")
            
            # El botón indica "Follow"
            if bl_follow:
                # Ajustar coordenadas de captura de popover
                

                # Obtener número de "seguidos" y "seguidores" del seguidor
                tt_act_seg_seguidor()
                
                # Calcular ratio del seguidor
                tmp_ratio = gen_functions.gen_act_ratio(tt_num_seguidos_seguidor, tt_num_seguidores_seguidor)

                # Si el ratio es igual o mayor al aceptado y cumple el mínimo de "seguidos", seguir usuario
                if tmp_ratio >= tt_ratio_min and tt_num_seguidos_seguidor >= tt_sig_min:
                    # Asignar las coordenas del centro del botón a la variable genérica con coordenadas en dónde hacer click
                    gen_functions.gen_camb_coords(coords_btn)
                    
                    # Click sobre el botón "Follow"
                    gen_functions.gen_click_spec(0.25)
                    
                    # Aumentar contador
                    cont_seg += 1
            
            # Cambiar bool
            bl_prim_usr = True

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
