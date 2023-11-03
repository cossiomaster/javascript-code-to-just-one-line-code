import re
import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import pyperclip

def convertir_a_una_linea():
    codigo_js = entrada_js.get("1.0", "end-1c")  # Obtiene el código de la primera caja de texto
    # Realiza la conversión
    codigo_js = re.sub(r'//.*', '', codigo_js)
    codigo_js = re.sub(r'/\*.*?\*/', '', codigo_js, flags=re.DOTALL)
    codigo_js = re.sub(r'\s+', ' ', codigo_js)
    codigo_js = codigo_js.strip()
    codigo_js = codigo_js.replace('\n', '')  # Elimina los saltos de línea
    # Muestra el código modificado en la segunda caja de texto
    salida_js.delete("1.0", "end")
    salida_js.insert("1.0", codigo_js)

def borrar_texto():
    salida_js.delete("1.0", "end")

def copiar_texto():
    codigo_copiado = salida_js.get("1.0", "end-1c")
    pyperclip.copy(codigo_copiado)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Convertir JavaScript a una línea")
ventana.configure(bg="black")  # Establecer el fondo de la ventana en negro brillante

# Caja de texto para ingresar el código JavaScript
entrada_js = scrolledtext.ScrolledText(ventana, height=10, width=40, bg="black", fg="lime green")  # Fondo negro brillante, letras verdes brillantes
entrada_js.pack()

# Crear un marco para los botones
marco_botones = tk.Frame(ventana, bg="black")  # Fondo del marco en negro brillante
marco_botones.pack()

# Botón para realizar la conversión
boton_convertir = tk.Button(marco_botones, text="Convertir", command=convertir_a_una_linea, bg="dark red", fg="white")  # Fondo rojo oscuro, letras blancas
boton_convertir.pack(side="left")

# Botón para borrar el texto en la segunda caja
boton_borrar = tk.Button(marco_botones, text="Borrar", command=borrar_texto, bg="dark red", fg="white")  # Fondo rojo oscuro, letras blancas
boton_borrar.pack(side="left")

# Botón para copiar el texto en la segunda caja
boton_copiar = tk.Button(marco_botones, text="Copiar", command=copiar_texto, bg="dark red", fg="white")  # Fondo rojo oscuro, letras blancas
boton_copiar.pack(side="left")

# Caja de texto para mostrar el código modificado con barra de desplazamiento horizontal
salida_js = scrolledtext.ScrolledText(ventana, height=10, width=40, wrap="none", bg="black", fg="lime green")  # Fondo negro brillante, letras verdes brillantes
salida_js.pack()

ventana.mainloop()
