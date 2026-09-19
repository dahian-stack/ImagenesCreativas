import tkinter as tk
from tkinter import ttk

from clase_aplicacion.personal_tecnico import crear_personal
from clase_aplicacion.equipo_tecnico import crear_equipos
from clase_aplicacion.localizaciones import crear_localizaciones
from clase_aplicacion.plan_rodaje import crear_rodaje


class Aplicacion:

    def __init__(self, ventana):

        self.ventana = ventana

        # Configuración de la ventana
        self.ventana.title("Imágenes Creativas S.A.")
        self.ventana.geometry("1000x750")
        self.ventana.configure(bg="#F5F0FA")

        # Título
        titulo = tk.Label(
            ventana,
            text="IMÁGENES CREATIVAS S.A.",
            font=("Arial", 22, "bold"),
            bg="#F5F0FA",
            fg="#6A4C93"
        )

        titulo.pack(pady=10)

        subtitulo = tk.Label(
            ventana,
            text="Sistema de administración de proyectos audiovisuales",
            font=("Arial", 11),
            bg="#F5F0FA",
            fg="#555555"
        )

        subtitulo.pack()

        # Crear las pestañas
        pestañas = ttk.Notebook(ventana)

        pestañas.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # Crear los espacios de cada módulo
        personal = ttk.Frame(pestañas)
        equipos = ttk.Frame(pestañas)
        localizaciones = ttk.Frame(pestañas)
        rodaje = ttk.Frame(pestañas)

        # Agregar las pestañas
        pestañas.add(
            personal,
            text="  Personal  "
        )

        pestañas.add(
            equipos,
            text="  Equipos  "
        )

        pestañas.add(
            localizaciones,
            text="  Localizaciones  "
        )

        pestañas.add(
            rodaje,
            text="  Plan de Rodaje  "
        )

        # Llamar a cada módulo
        crear_personal(personal)
        crear_equipos(equipos)
        crear_localizaciones(localizaciones)
        crear_rodaje(rodaje)


# Programa principal
ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()