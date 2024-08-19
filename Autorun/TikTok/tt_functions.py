from Autorun.Generic import gen_functions
from Autorun.Chromium import chr_functions
import pyautogui
import time

# Perfil TikTok
def tt_perfil_bot():
    pyautogui.moveTo(976, 32)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(976, 84)
    pyautogui.click()
    time.sleep(10)

# "Seguidos" del bot y seguidores del bot
def tt_siguiendo_pos():
    pyautogui.moveTo(142, 246)
    pyautogui.click()
    time.sleep(10)

# "Seguidores" del bot y seguidores del seguidor del bot
def tt_seguidores_pos():
    pyautogui.moveTo(286, 246)
    pyautogui.click()
    time.sleep(10)

# Colocar cursor sobre "Followers"
def tt_seguidores_pos_cur():
    pyautogui.moveTo(286, 246)
    time.sleep(1)

# Cerrar ventana chica
def tt_cerrar_ventana_ch():
    pyautogui.moveTo(90, 540)
    pyautogui.click()
    time.sleep(1)

# Posición en ventana chica
def tt_pos_ventana_ch():
    pyautogui.moveTo(610, 200)
    time.sleep(0.25)

# Número de seguidos y seguidores del bot en sesión actual y previa
tt_num_seguidos_bot = 0
tt_num_seguidores_bot = 0
tt_num_seguidores_bot_prev = 0

# Obtener número de seguidores del bot de sesión previa
def tt_act_seguidores_bot_prev():
    global tt_num_seguidores_bot_prev
    
    # Obtener cifra desde archivo de texto
    tt_num_seguidores_bot_prev = gen_functions.gen_busq_txt('Autorun/TikTok/Refs/tt_ref.txt', 1)
    
    # Convertir cifra a entero
    tt_num_seguidores_bot_prev = int(tt_num_seguidores_bot_prev)

# Coordenas para "Followers", "Following" y "Likes" del bot y seguidores del bot
tt_ffl_box = [90, 234, 410, 24]

# Número de seguidos y seguidores del seguidor
tt_num_seguidos_seguidor = 0
tt_num_seguidores_seguidor = 0

# Actualizar "seguidos" y "seguidores" del bot
def tt_act_seg_bot():
    global tt_num_seguidos_bot, tt_num_seguidores_bot
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(tt_ffl_box)
    
    tt_num_seguidos_bot = gen_functions.gen_cifra(tmp_img, "Following")
    tt_num_seguidores_bot = gen_functions.gen_cifra(tmp_img, "Followers")

# Limpir seguidos del bot
def tt_limp_seguidos_bot():
    # Obtener fecha y hora de sesión previa
    fecha_prev = gen_functions.gen_busq_txt('Autorun/TikTok/Refs/tt_ref.txt', 0)
    
    # Obtener diferencia de horas entre fecha previa y actual
    dif_hr = gen_functions.gen_dif_hr(fecha_prev)
    
    # Limpiar "seguidos" si aplica
    if dif_hr > 24:
        # Mientras hayan más de 4 usuarios siguiendo
        while tt_num_seguidos_bot > 4:
            # Ir a "seguidos" del bot
            tt_siguiendo_pos()
            
            # Bool de primer usuario evaluado
            bl_prim_usr = False
            
            # Dejar de seguir usuarios
            for iter_seg in range(tt_num_seguidos_bot - 4):
                
                if bl_prim_usr:
                    # Colocar cursor para desplazar hacia abajo
                    tt_pos_ventana_ch()
                    
                    # Desplazar hacia el siguiente seguidor
                    gen_functions.gen_desp_usr(tt_seg_box)
                
                # Encontrar nombre del seguidor y asignar coordenas a variable genérica
                gen_functions.gen_prim_usr(tt_seg_box)
                
                # Asignar coordenas del centro del botón
                coords_btn = tt_aj_seg_box()
                
                # Asignar las coordenas del centro del botón a la variable genérica con coordenadas en dónde hacer click
                gen_functions.gen_camb_coords(coords_btn)
                
                # Click sobre el botón
                gen_functions.gen_click_spec(0.25)
                
                # Cambiar bool
                bl_prim_usr = True
            
            # Recargar página
            chr_functions.chr_rec_pag()
            
            # Capturar número de "seguidos" del bot
            tt_act_seg_bot()

tt_dif_seguidores_bot = 0

# Calcular diferencia de seguidores del bot (iteración máxima)
def tt_calc_dif_seg_bot():
    global tt_dif_seguidores_bot
    
    tt_dif_seguidores_bot = tt_num_seguidores_bot - tt_num_seguidores_bot_prev
    
    if tt_dif_seguidores_bot < 5:
        tt_dif_seguidores_bot = 15

# Actualizar "seguidos" y "seguidores" del seguidor del bot
def tt_act_seg_seguidor():
    global tt_num_seguidos_seguidor, tt_num_seguidores_seguidor
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(tt_ffl_box)
    
    tt_num_seguidos_seguidor = gen_functions.gen_cifra(tmp_img, "Following")
    tt_num_seguidores_seguidor = gen_functions.gen_cifra(tmp_img, "Followers")

# Evaluar si los seguidores son privados
def tt_seguidores_priv():
    # Colocar el cursor sobre "Followers"
    tt_seguidores_pos_cur()
    
    # Primera captura de pantalla
    tmp_scr1 = gen_functions.gen_capt_pant()
    
    # Abrir "Followers"
    tt_seguidores_pos()
    
    # Segunda captura de pantalla
    tmp_scr2 = gen_functions.gen_capt_pant()
    
    # Evaluar si hay cambio
    gen_functions.gen_camb_entn(tmp_scr1, tmp_scr2)

# Parámetros para decidir si seguir o no
tt_ratio_min = 1.8
tt_seg_min = 900

# Campo de visión en ventana de seguidores y seguidos
tt_seg_box = [320, 162, 224, 200]

# Elegir a un seguidor del bot
def tt_elegir_seguidor_bot():
    # Máximo de iteraciones
    tt_calc_dif_seg_bot()
    
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Iteraciones entre seguidores del bot
    for iter_seg in range(tt_dif_seguidores_bot):
        # Desplazar hacia abajo después del primer seguidor
        if bl_prim_usr:
            # Colocar cursor para desplazar hacia abajo
            tt_pos_ventana_ch()
            
            # Desplazar hacia el siguiente seguidor
            gen_functions.gen_desp_usr(tt_seg_box)
        
        # Encontrar nombre del seguidor y asignar coordenas
        gen_functions.gen_prim_usr(tt_seg_box)
        
        # Ir a perfil del seguidor en nueva pestaña
        gen_functions.gen_ab_click_spec(25)
        
        # Obtener número de "seguidos" y "seguidores" del seguidor
        tt_act_seg_seguidor()
        
        # Calcular ratio del seguidor
        tmp_ratio = gen_functions.gen_act_ratio(tt_num_seguidos_seguidor, tt_num_seguidores_seguidor)
        
        # Si el ratio es igual o mayor al aceptado, cumple el mínimo de "seguidos" y los seguidores son públicos, terminar función
        if tmp_ratio >= tt_ratio_min and tt_num_seguidos_seguidor >= tt_seg_min:
            # Evaluar si los "seguidores" son privados
            tt_seguidores_priv()
            
            if gen_functions.gen_camb_bl:
                # Cerrar pestaña anterior
                chr_functions.chr_pestana_anterior()
                chr_functions.chr_cerrar_pestana()
                
                # Restaurar bool a False
                gen_functions.gen_f_camb_bl(False)
                
                break
        # No se cumplen los parámetros
        else:
            chr_functions.chr_cerrar_pestana()
        
        # Cambiar bool
        bl_prim_usr = True

# Coordenas del botón "Follow", "Following", "Follow Back" de ventana de seguidores y seguidos
tt_bot_seg_box = [648, 186, 94, 22]

# Ajustar botón "Follow", "Following", "Follow back" de ventana de seguidores y seguidos
def tt_aj_seg_box():
    global tt_bot_seg_box
    
    # Desplazar verticalmente caja de captura de imagen para el botón
    tt_bot_seg_box[1] = gen_functions.gen_centro_xy[1]
    
    # Calcular centro del botón y retornar coordenadas
    return gen_functions.gen_calc_cent_rtn(tt_bot_seg_box)

# Evaluar si una palabra está presente
def tt_bl_pal(pal_ref):
    # Capturar área de la pantalla con el botón
    tmp_img = gen_functions.gen_capt_spec_pant(tt_bot_seg_box)
    
    # Obtener texto de la imagen
    tmp_txt = gen_functions.gen_text_img(tmp_img)
    
    # Evaluar si la palabra está presente en la imagen
    if tmp_txt == pal_ref:
        return True
    else:
        return False

# Ciclo de búsqueda
def tt_ciclo_busqueda(val_busq):
    # Máximo de iteraciones
    max_iter = tt_num_seguidores_seguidor
    
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Contador de seguidos
    cont_seg = 0
    
    # Iteraciones entre seguidores del seguidor
    for iter_seg in range(max_iter):
        if cont_seg == val_busq:
            break
        else:
            # Desplazar hacia abajo después del primer seguidor
            if bl_prim_usr:
                # Colocar cursor para desplazar hacia abajo
                tt_pos_ventana_ch()
                
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
                # Ir a perfil del seguidor en nueva pestaña
                gen_functions.gen_ab_click_spec(20)
                
                # Obtener número de "seguidos" y "seguidores" del seguidor
                tt_act_seg_seguidor()
                
                # Calcular ratio del seguidor
                tmp_ratio = gen_functions.gen_act_ratio(tt_num_seguidos_seguidor, tt_num_seguidores_seguidor)
                
                # Cerrar pestaña
                chr_functions.chr_cerrar_pestana()
                
                # Si el ratio es igual o mayor al aceptado y cumple el mínimo de "seguidos", seguir usuario
                if tmp_ratio >= tt_ratio_min and tt_num_seguidos_seguidor >= tt_seg_min:
                    # Asignar las coordenas del centro del botón a la variable genérica con coordenadas en dónde hacer click
                    gen_functions.gen_camb_coords(coords_btn)
                    
                    # Click sobre el botón "Follow"
                    gen_functions.gen_click_spec(0.25)
                    
                    # Aumentar contador
                    cont_seg += 1
                    
            # Cambiar bool
            bl_prim_usr = True

# Esperar hasta siguiente ciclo de búsqueda
def tt_espera(val_tiempo):
    time.sleep(val_tiempo)