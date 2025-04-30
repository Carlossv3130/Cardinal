import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def renombrar_automaticamente(carpeta):
    archivos = os.listdir(carpeta)
    archivos = [f for f in archivos if os.path.isfile(os.path.join(carpeta, f))]

    for i, archivo in enumerate(archivos, start=1):
        ext = os.path.splitext(archivo)[1]
        nuevo_nombre = f"archivo_{i}{ext}"
        os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo_nombre))

    messagebox.showinfo("¡Listo!", "Archivos renombrados automáticamente.")

def renombrar_personalizado(carpeta):
    archivos = os.listdir(carpeta)
    archivos = [f for f in archivos if os.path.isfile(os.path.join(carpeta, f))]

    base = simpledialog.askstring("Nombre base", "Escribe un nombre base para los archivos (ej: factura, informe):")
    if not base:
        return

    for i, archivo in enumerate(archivos, start=1):
        ext = os.path.splitext(archivo)[1]
        nuevo_nombre = f"{base}_{i}{ext}"
        os.rename(os.path.join(carpeta, archivo), os.path.join(carpeta, nuevo_nombre))

    messagebox.showinfo("¡Listo!", "Archivos renombrados con nombre base.")

def seleccionar_carpeta(opcion):
    carpeta = filedialog.askdirectory()
    if carpeta:
        if opcion == 'auto':
            renombrar_automaticamente(carpeta)
        elif opcion == 'personal':
            renombrar_personalizado(carpeta)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Renombrador de Archivos")
ventana.geometry("400x200")
ventana.resizable(False, False)

etiqueta = tk.Label(ventana, text="¿Cómo deseas renombrar los archivos?", font=("Arial", 12))
etiqueta.pack(pady=20)

boton_auto = tk.Button(ventana, text="✅ Renombrar Automáticamente", width=30, command=lambda: seleccionar_carpeta('auto'))
boton_auto.pack(pady=5)

boton_personal = tk.Button(ventana, text="📝 Renombrar con Nombre Base", width=30, command=lambda: seleccionar_carpeta('personal'))
boton_personal.pack(pady=5)

ventana.mainloop()
