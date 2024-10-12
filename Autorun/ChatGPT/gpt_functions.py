from Autorun.System import sys_functions
from Autorun.Generic import gen_functions
from Autorun.Chromium import chr_functions
import pyautogui
import time

# Coordenadas de input box (primera petición)
gpt_cord_input_box_1 = [500, 545]

# Coordenadas de input box
gpt_cord_input_box_2 = [500, 545]

# Usar input box
def gpt_input_box(tmp_coords):
    gen_functions.gen_centro_xy = tmp_coords
    gen_functions.gen_click_spec(1)

# Campo de captura de logo
gpt_logo_box = [115, 160, 145, 300]

# Campo de captura de respuesta
gpt_resp_box = [180, 160, 160, 22]

# Petición de formato de respuesta
gpt_ini_txt = "Únicamente una línea de respuesta, no más. Responde con, La respuesta es: , seguido únicamente con la letra que corresponda en orden alfabético a la respuesta de la pregunta (la primera opción es a, la segunda b, así subsecuentemente): "

# Pregunta capturada desde cámara
gpt_capt_txt = "En un apaciente con un absceso dental que recibe tratamiento con clindamicina, ¿Cuál sería el efecto tóxico que más frecuentemente esperaría?. A) Anemia B) Neuropatía periférica C) Rash D) Hepatotoxiccidad"

# Pregunta a ingresar
gpt_preg_txt = ""

# Respuesta capturada
gpt_resp_txt = ""

# Coordenadas para desplazar página
gpt_cord_desp = [500, 100]

# Desplazar hasta el fondo
def gpt_fin_pag():
    gen_functions.gen_centro_xy = gpt_cord_desp
    gen_functions.gen_click_spec(0.5)
    chr_functions.chr_fin_pag()

# Coordenadas para cerrar pop up de inicio de sesión
gpt_cord_cerr_popup = [500, 450]

# Cerrar pop up de inicio de sesión
def gpt_cerr_popup():
    gen_functions.gen_centro_xy = gpt_cord_cerr_popup
    gen_functions.gen_click_spec(2)

# Ajustar coordenadas de campo de captura de respuesta
def gpt_aj_capt_resp():
    # Asignar coordenadas del centro del logo de ChatGPT en chat
    gen_functions.gen_coinc_imgs(gpt_logo_box, 'Autorun/ChatGPT/Refs/logo.png')
    
    # Ajustar caja de captura de texto (respuesta)
    gpt_resp_box[1] = gen_functions.gen_centro_xy[1] - 10

def gpt_ult_ch():
    global gpt_resp_txt
    
    # Limpiar espacios y líneas en blanco
    gpt_resp_txt = gen_functions.gen_del_lin(gpt_resp_txt)
    
    # Capturar último carácter
    gpt_resp_txt = gpt_resp_txt[-1]

# Asignar respuesta obtenida
def gpt_capt_resp():
    global gpt_resp_txt
    
    # Capturar un área con la respuesta
    tmp_img = gen_functions.gen_capt_spec_pant(gpt_resp_box)
    
    # Obtener texto de la imagen
    gpt_resp_txt = gen_functions.gen_text_img(tmp_img)

# Mostrar la respuesta
def gpt_mst_resp():
    print(gpt_resp_txt)

# Capturar pregunta desde cámara
"""def gpt_cam_capt():
    global gpt_capt_txt
    
    while True:
        # Esperar señal de captura
        
        
        # Se ha capturado texto
        if gpt_capt_txt != "":
            #Limpiar líneas en blanco en el texto
            gpt_capt_txt = gen_functions.gen_del_lin(gpt_capt_txt)
            
            # Reemplazar saltos de línea por espacios en el texto
            gpt_capt_txt = gen_functions.gen_reemp_salt(gpt_capt_txt)
            
            break"""

# Generar pregunta
def gpt_gen_preg():
    global gpt_preg_txt, gpt_ini_txt, gpt_capt_txt
    
    # Unir petición y pregunta
    gpt_preg_txt = gpt_ini_txt + gpt_capt_txt

# Capturar preguntas y expresar respuestas indeterminadamente
def gpt_preg_resp():
    global gpt_cord_input_box_1, gpt_cord_input_box_2
    
    prim_pet = True
    
    while True:
        if prim_pet: 
            # Cerrar posible pop up
            gpt_cerr_popup()
            
            # Colocar cursor sobre input box
            gpt_input_box(gpt_cord_input_box_1)
            
            prim_pet = False
        
        # Esperar a capturar pregunta
        #gpt_cam_capt()
        
        # Generar petición con pregunta
        gpt_gen_preg()
        
        # Enviar pregunta
        gen_functions.gen_escribir_msg(gpt_preg_txt, 20)
        
        # Cerrar posible pop up
        gpt_cerr_popup()
        
        # Ajustar coordenadas de campo de captura de respuesta
        gpt_aj_capt_resp()
        
        # Capturar respuesta
        gpt_capt_resp()
        
        # Conservar letra de la respuesta en captura de texto
        gpt_ult_ch()
        
        # Expresar respuesta
        gpt_mst_resp()
        
        # Colocar cursor sobre input box
        gpt_input_box(gpt_cord_input_box_2)
        
        #----------------------------------------------
        input('')

# Ciclo de preguntas y respuestas
def gpt_ciclo_resp():
    # Abrir Chromium
    sys_functions.sys_abrir_chr()
    
    # Cerrar ventana de restaurar páginas
    chr_functions.chr_error_cerrar()
    
    # Ir a ChatGPT
    chr_functions.chr_bm_gpt()
    
    # Capturar preguntas y expresar respuestas indeterminadamente 
    gpt_preg_resp()
