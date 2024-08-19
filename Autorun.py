from Autorun.TikTok import tt_functions
from Autorun.System import sys_functions
from Autorun.Chromium import chr_functions
from Autorun.Generic import gen_functions

def tt_ciclo_busqueda(val_seg, val_tiempo):
    # Abrir TikTok
    sys_functions.sys_abrir_tt()
    
    # Cerrar ventana de restaurar páginas
    chr_functions.chr_error_cerrar()
    
    # Ir a perfil de TikTok del bot
    tt_functions.tt_perfil_bot()
    
    # Obtener número de seguidos, seguidores y seguidores de sesión previa, del bot
    tt_functions.tt_act_seg_bot()
    tt_functions.tt_act_seguidores_bot_prev()
    
    # Revisar tiempo desde ultima sesión,limpiar "seguidos" si aplica
    tt_functions.tt_limp_seguidos_bot()
    
    # Ir a seguidores del bot
    tt_functions.tt_seguidores_pos()
    
    # Elegir un seguidor del bot
    tt_functions.tt_elegir_seguidor_bot()
    
    # Ir a seguidores del seguidor
    tt_functions.tt_seguidores_pos()
    
    # Seguir seguidores del seguidor
    tt_functions.tt_ciclo_busqueda(val_seg)
    
    # Cerrar ventana
    sys_functions.sys_cerrar_ventana()
    
    # Actualizar registro de sesión a la hora actual
    gen_functions.gen_act_fecha('Autorun/TikTok/Refs/tt_ref.txt')
    
    # Esperar hasta reanudar el ciclo
    tt_functions.tt_espera(val_tiempo)

# Ejecutar ciclo indefinidamente
while True:
   tt_ciclo_busqueda(50, 30*60)
