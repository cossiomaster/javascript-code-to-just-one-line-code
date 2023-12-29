import tkinter as tk
from tkinter import Scrollbar

def copiar_texto():
    texto = cuadro_texto1.get("1.0", "end-1c")
    cuadro_texto2.delete(1.0, "end")
    cuadro_texto2.insert("1.0", texto)

def pegar_texto():
    texto = cuadro_texto2.get("1.0", "end-1c")
    cuadro_texto1.delete(1.0, "end")
    cuadro_texto1.insert("1.0", texto)

def borrar_texto():
    cuadro_texto1.delete(1.0, "end")
    cuadro_texto2.delete(1.0, "end")

def limitar_caracteres():
    try:
        num_caracteres = int(cuadro_num_caracteres.get())
        texto = cuadro_texto1.get("1.0", "end-1c")
        
        # Dividir el texto en líneas cada num_caracteres caracteres y agregar \n al final de cada línea
        texto_formateado = '\n'.join([texto[i:i+num_caracteres] + "\\n" for i in range(0, len(texto), num_caracteres)])
        
        cuadro_texto2.delete(1.0, "end")
        cuadro_texto2.insert("1.0", texto_formateado)
    except ValueError:
        pass  # Manejar el caso en que el usuario no ingrese un número

def aplanar_texto():
    texto = cuadro_texto2.get("1.0", "end-1c").replace('\n', ' ')
    cuadro_texto2.delete(1.0, "end")
    cuadro_texto2.insert("1.0", texto)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")

# Crear el cuadro de texto 1
etiqueta_cuadro1 = tk.Label(ventana, text="Ingrese texto aquí")
etiqueta_cuadro1.pack()

cuadro_texto1 = tk.Text(ventana, height=5, width=40)
cuadro_texto1.pack()

# Crear el cuadro de entrada para el número de caracteres
etiqueta_num_caracteres = tk.Label(ventana, text="Ingresa número de caracteres:")
etiqueta_num_caracteres.pack()

cuadro_num_caracteres = tk.Entry(ventana)
cuadro_num_caracteres.pack()

# Crear botones
boton_borrar = tk.Button(ventana, text="Borrar", command=borrar_texto)
boton_borrar.pack()

boton_pegar = tk.Button(ventana, text="Pegar", command=pegar_texto)
boton_pegar.pack()

boton_copiar = tk.Button(ventana, text="Copiar", command=copiar_texto)
boton_copiar.pack()

boton_limitar = tk.Button(ventana, text="Limitar Caracteres", command=limitar_caracteres)
boton_limitar.pack()

boton_aplanar = tk.Button(ventana, text="Aplanar Texto", command=aplanar_texto)
boton_aplanar.pack()

# Crear el cuadro de texto 2 con barra de desplazamiento horizontal
etiqueta_cuadro2 = tk.Label(ventana, text="Resultado:")
etiqueta_cuadro2.pack()

cuadro_texto2 = tk.Text(ventana, height=5, width=40, wrap='none')
scroll_horizontal = tk.Scrollbar(ventana, orient='horizontal', command=cuadro_texto2.xview)
scroll_horizontal.pack(fill='x')
cuadro_texto2.configure(xscrollcommand=scroll_horizontal.set)

cuadro_texto2.pack()

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()
