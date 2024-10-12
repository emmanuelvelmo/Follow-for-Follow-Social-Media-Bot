from Autorun.System import sys_functions
from Autorun.Generic import gen_functions
from Autorun.Chromium import chr_functions
import pyautogui
import time

# Perfil de Instagram
def inst_perfil_bot():
    pyautogui.moveTo(35, 525)
    pyautogui.click()
    time.sleep(10)

# "Seguidores" del bot y seguidores del seguidor del bot
def inst_seguidores_pos():
    pyautogui.moveTo(515, 115)
    pyautogui.click()
    time.sleep(10)

# "Seguidos" del bot y seguidores del bot
def inst_siguiendo_pos():
    pyautogui.moveTo(640, 115)
    pyautogui.click()
    time.sleep(10)

# Cerrar pop up
def inst_cerrar_pop_up():
    pyautogui.moveTo(730, 60)
    pyautogui.click()
    time.sleep(2)

# Posición en pop up
def inst_pos_pop_up():
    pyautogui.moveTo(575, 205)
    time.sleep(1)

# Número de seguidos y seguidores del bot en sesión actual y previa
inst_num_seguidos_bot = 0
inst_num_seguidores_bot = 0
inst_num_seguidores_bot_prev = 0

# Obtener número de seguidores del bot de sesión previa
def inst_act_seguidores_bot_prev():
    global inst_num_seguidores_bot_prev
    
    # Obtener cifra desde archivo de texto y convertir a entero
    inst_num_seguidores_bot_prev = int(gen_functions.gen_busq_txt('Autorun/Instagram/Refs/inst_ref.txt', 1))

# Coordenas para "Followers", "Following" y "Likes" del bot
inst_ffl_box = [390, 95, 285, 35]

# Número de seguidos y seguidores del seguidor
inst_num_seguidos_seguidor = 0
inst_num_seguidores_seguidor = 0

# Actualizar "seguidores" y "seguidos" del bot
def inst_act_seg_bot():
    global inst_num_seguidos_bot, inst_num_seguidores_bot
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(inst_ffl_box)

    # Actualizar variables
    inst_num_seguidos_bot = gen_functions.gen_cifra(tmp_img, "Following")
    inst_num_seguidores_bot = gen_functions.gen_cifra(tmp_img, "Followers")

inst_dif_seguidores_bot = 0

# Calcular diferencia de seguidores del bot (iteración máxima)
def inst_calc_dif_seg_bot():
    global inst_dif_seguidores_bot
    
    inst_dif_seguidores_bot = inst_num_seguidores_bot - inst_num_seguidores_bot_prev
    
    if inst_dif_seguidores_bot < 5:
        inst_dif_seguidores_bot = 15

# Actualizar "seguidores" y "seguidos" del seguidor del bot
def inst_act_seg_seguidor():
    global inst_num_seguidos_seguidor, inst_num_seguidores_seguidor
    
    # Capturar región de pantalla
    tmp_img = gen_functions.gen_capt_spec_pant(inst_popov_dat_box)
    
    # Corregir saltos de línea en texto
    gen_functions.gen_corr_lin(tmp_img)

    # Actualizar variables
    inst_num_seguidos_seguidor = gen_functions.gen_cifra(tmp_img, "Following")
    inst_num_seguidores_seguidor = gen_functions.gen_cifra(tmp_img, "Followers")

# Coordenas de caja de captura de "posts", "seguidores" y "seguidos" en popover en listas de seguidos y seguidores
inst_popov_dat_box = [355,335, 300, 50]

# Coordenas de caja de captura de tipo de cuenta en popover en listas de seguidos y seguidores
inst_popov_tip_box = [325, 395, 360,115]

# Evaluar si la cuenta es privada
def inst_seguidores_priv():
    # Capturar área de popover con el tipo de cuenta
    tmp_img = gen_functions.gen_capt_spec_pant(inst_popov_tip_box)
    
    # Obtener texto de la imagen
    tmp_txt = gen_functions.gen_text_img(tmp_img)
    
    # Buscar 'private' en texto
    return 'private' in tmp_txt

# Ajustar popover de seguidos y seguidores
def inst_aj_popov_box():
    # Desplazar verticalmente cajas de captura de imagen en el popover
    inst_popov_dat_box[1] = gen_functions.gen_centro_xy[1] + 100
    inst_popov_tip_box[1] = gen_functions.gen_centro_xy[1] + 160

# Coordenas del botón "Follow", "Following", "Follow Back", "Friends", "Remove" de ventana de seguidos y seguidores
inst_bot_seg_box = [645, 230, 70, 25]

# Ajustar botón "Follow", "Following", "Follow back" de ventana de seguidos y seguidores y retornar cordenadas de su centro
def inst_aj_seg_box():
    global inst_bot_seg_box
    
    # Desplazar verticalmente caja de captura de imagen para el botón
    inst_bot_seg_box[1] = gen_functions.gen_centro_xy[1] - 2
    
    # Calcular centro del botón y retornar coordenadas
    return gen_functions.gen_calc_cent_rtn(inst_bot_seg_box)

# Evaluar si una palabra está presente en el botón
def inst_bl_btn(pal_ref):
    # Capturar área de la pantalla con el botón
    tmp_img = gen_functions.gen_capt_spec_pant(inst_bot_seg_box)
    
    # Obtener texto de la imagen
    tmp_txt = gen_functions.gen_text_img(tmp_img)
    
    # Evaluar si la palabra está presente en la imagen
    if tmp_txt == pal_ref:
        return True
    else:
        return False

# Actualizar fecha en txt
def inst_act_fecha():
    # Obtener fecha y hora de sesión previa
    fecha_prev = gen_functions.gen_busq_txt('Autorun/Instagram/Refs/inst_ref.txt', 0)
    
    # Obtener diferencia de horas entre fecha previa y actual
    dif_hr = gen_functions.gen_dif_hr(fecha_prev)
    
    # Si han pasado por lo menos 36 horas desde la última limpieza
    if dif_hr >= 36:
        # Actualizar fecha en txt
        gen_functions.gen_act_fecha('Autorun/Instagram/Refs/inst_ref.txt', 0)

# Actualizar número de seguidores del bot en txt
def inst_act_seg_txt():
    gen_functions.gen_act_txt('Autorun/Instagram/Refs/inst_ref.txt', 1, inst_num_seguidores_bot)

# Parámetros para decidir si seguir o no
inst_ratio_min = 3
inst_sig_min = 900

# Campo de visión en ventana de seguidos y seguidores
inst_seg_box = [320, 205, 190, 120]

# Limpiar seguidos del bot
def inst_limp_seguidos_bot():
    # Obtener fecha y hora de sesión previa
    fecha_prev = gen_functions.gen_busq_txt('Autorun/Instagram/Refs/inst_ref.txt', 0)
    
    # Obtener diferencia de horas entre fecha previa y actual
    dif_hr = gen_functions.gen_dif_hr(fecha_prev)
    
    # Limpiar "seguidos" si aplica
    if dif_hr >= 36:
        if inst_num_seguidos_bot > 5:
            # Mientras hayan más de 5 usuarios siguiendo
            while inst_num_seguidos_bot > 5:
                # Ir a "seguidos" del bot
                inst_siguiendo_pos()
                
                # Bool de primer usuario evaluado
                bl_prim_usr = False
                
                # Dejar de seguir usuarios
                for iter_seg in range(inst_num_seguidos_bot - 5):
                    
                    if bl_prim_usr:
                        # Colocar cursor para desplazar hacia abajo
                        inst_pos_pop_up()
                        
                        # Desplazar hacia el siguiente seguidor
                        gen_functions.gen_desp_usr(inst_seg_box)
                    
                    # Encontrar nombre del seguidor y asignar coordenas a variable genérica
                    gen_functions.gen_prim_usr(inst_seg_box)
                    
                    # Asignar coordenas del centro del botón y ajustar caja de captura de texto de botón
                    coords_btn = inst_aj_seg_box()
                    
                    # Asignar las coordenas del centro del botón a la variable genérica con coordenadas en dónde hacer click
                    gen_functions.gen_camb_coords(coords_btn)
                    
                    # Click sobre el botón
                    gen_functions.gen_click_spec(0.25)
                    
                    # Cambiar bool
                    bl_prim_usr = True
                
                # Recargar página
                chr_functions.chr_rec_pag()
                
                # Capturar número de "seguidos" del bot
                inst_act_seg_bot()

# Elegir a un seguidor del bot
def inst_elegir_seguidor_bot():
    # Calcular máximo de iteraciones
    inst_calc_dif_seg_bot()
    
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Iteraciones entre seguidores del bot
    for iter_seg in range(inst_dif_seguidores_bot):
        # Desplazar hacia abajo después del primer seguidor
        if bl_prim_usr:
            # Colocar cursor para desplazar hacia abajo
            inst_pos_pop_up()
            
            # Desplazar hacia el siguiente seguidor
            gen_functions.gen_desp_usr(inst_seg_box)
        
        # Encontrar nombre del seguidor y asignar coordenas a variable genérica
        gen_functions.gen_prim_usr(inst_seg_box)

        # Ajustar coordenadas de cajas de captura de popover
        inst_aj_popov_box()

        # Colocar cursor sobre el nombre de usuario
        gen_functions.gen_cur_spec()

        # Evaluar si los seguidores son privados desde el popover
        bl_priv = inst_seguidores_priv()

        # Si la cuenta no es privada
        if not bl_priv:
            # Obtener número de "seguidores" y "seguidos" del seguidor desde el popover
            inst_act_seg_seguidor()

            # Calcular ratio del seguidor
            tmp_ratio = gen_functions.gen_act_ratio(inst_num_seguidos_seguidor, inst_num_seguidores_seguidor)
        
            # Si el ratio es igual o mayor al aceptado, cumple el mínimo de "seguidos"
            if tmp_ratio >= inst_ratio_min and inst_num_seguidos_seguidor >= inst_sig_min:
                # Ir a perfil del seguidor en nueva pestaña
                gen_functions.gen_ab_click_spec(25)

                # Cerrar pestaña anterior
                chr_functions.chr_pestana_anterior()
                chr_functions.chr_cerrar_pestana()
                
                break
        
        # Cambiar bool
        bl_prim_usr = True

# Ciclo de búsqueda
def inst_ciclo_busqueda(val_busq):
    # Bool de primer usuario evaluado
    bl_prim_usr = False
    
    # Contador de seguidos
    cont_seg = 0
    
    # Iteraciones entre seguidores del seguidor
    for iter_seg in range(inst_num_seguidores_seguidor - 5):
        if cont_seg == val_busq:
            break
        else:
            # Desplazar hacia abajo después del primer seguidor
            if bl_prim_usr:
                # Colocar cursor para desplazar hacia abajo
                inst_pos_pop_up()
                
                # Desplazar hacia el siguiente seguidor
                gen_functions.gen_desp_usr(inst_seg_box)
            
            # Encontrar nombre del seguidor y asignar coordenas a variable genérica
            gen_functions.gen_prim_usr(inst_seg_box)
            
            # Asignar coordenas del centro del botón y ajustar caja de captura de texto de botón
            coords_btn = inst_aj_seg_box()
            
            # Evaluar si la palabra "Follow" está presente
            bl_follow = inst_bl_btn("Follow")
            
            # El botón indica "Follow"
            if bl_follow:
                # Ajustar coordenadas de captura de popover
                inst_aj_popov_box()

                # Colocar cursor sobre el nombre de usuario
                gen_functions.gen_cur_spec()

                # Obtener número de "seguidores" y "seguidos" del seguidor
                inst_act_seg_seguidor()
                
                # Calcular ratio del seguidor
                tmp_ratio = gen_functions.gen_act_ratio(inst_num_seguidos_seguidor, inst_num_seguidores_seguidor)

                # Si el ratio es igual o mayor al aceptado y cumple el mínimo de "seguidos", seguir usuario
                if tmp_ratio >= inst_ratio_min and inst_num_seguidos_seguidor >= inst_sig_min:
                    # Asignar las coordenas del centro del botón a la variable genérica con coordenadas en dónde hacer click
                    gen_functions.gen_camb_coords(coords_btn)
                    
                    # Click sobre el botón "Follow"
                    gen_functions.gen_click_spec(0.25)
                    
                    # Aumentar contador
                    cont_seg += 1
            
            # Cambiar bool
            bl_prim_usr = True

# Ciclo follow for follow
def inst_ciclo_bot(val_seg, val_tiempo):
    # Abrir Chromium
    sys_functions.sys_abrir_chr()
    
    # Cerrar ventana de restaurar páginas
    chr_functions.chr_error_cerrar()
    
    # Ir a Instagram
    chr_functions.chr_sit_web("https://www.instagram.com/", 30)
    
    # Ir a perfil de Instagram del bot
    inst_perfil_bot()
    
    # Obtener número de seguidos, seguidores y seguidores de sesión previa, del bot
    inst_act_seg_bot()
    inst_act_seguidores_bot_prev()
    
    # Revisar tiempo desde ultima sesión,limpiar "seguidos" si aplica
    inst_limp_seguidos_bot()
    
    # Ir a seguidores del bot
    inst_seguidores_pos()
    
    # Elegir un seguidor del bot
    inst_elegir_seguidor_bot()
    
    # Ir a seguidores del seguidor
    inst_seguidores_pos()
    
    # Seguir seguidores del seguidor
    inst_ciclo_busqueda(val_seg)
    
    # Cerrar ventana
    sys_functions.sys_cerrar_ventana()
    
    # Actualizar registro de sesión cada 36 horas o más
    inst_act_fecha()
    
    # Actualizar número de seguidores
    inst_act_seg_txt()
    
    # Esperar hasta reanudar el ciclo
    time.sleep(val_tiempo)
