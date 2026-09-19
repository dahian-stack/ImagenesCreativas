import tkinter as tk
from tkinter import messagebox


def crear_rodaje(ventana):

    tk.Label(
        ventana,
        text="PLAN DE RODAJE",
        font=("Arial", 16, "bold"),
        fg="#D95D39"
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=15
    )

    # Código de producción
    tk.Label(
        ventana,
        text="Código de producción:"
    ).grid(row=1, column=0, sticky="w", padx=20, pady=5)

    codigo = tk.Entry(ventana, width=40)
    codigo.grid(row=1, column=1, pady=5)

    # Día de rodaje
    tk.Label(
        ventana,
        text="Día de rodaje:"
    ).grid(row=2, column=0, sticky="w", padx=20, pady=5)

    dia = tk.Entry(ventana, width=40)
    dia.grid(row=2, column=1, pady=5)

    # Fecha
    tk.Label(
        ventana,
        text="Fecha:"
    ).grid(row=3, column=0, sticky="w", padx=20, pady=5)

    fecha = tk.Entry(ventana, width=40)
    fecha.grid(row=3, column=1, pady=5)

    # Hora inicio
    tk.Label(
        ventana,
        text="Horario de inicio:"
    ).grid(row=4, column=0, sticky="w", padx=20, pady=5)

    inicio = tk.Entry(ventana, width=40)
    inicio.grid(row=4, column=1, pady=5)

    # Hora fin
    tk.Label(
        ventana,
        text="Horario de finalización:"
    ).grid(row=5, column=0, sticky="w", padx=20, pady=5)

    fin = tk.Entry(ventana, width=40)
    fin.grid(row=5, column=1, pady=5)

    # Localización
    tk.Label(
        ventana,
        text="Localización:"
    ).grid(row=6, column=0, sticky="w", padx=20, pady=5)

    localizacion = tk.Entry(ventana, width=40)
    localizacion.grid(row=6, column=1, pady=5)

    # Escenas
    tk.Label(
        ventana,
        text="Escenas programadas:"
    ).grid(row=7, column=0, sticky="w", padx=20, pady=5)

    escenas = tk.Entry(ventana, width=40)
    escenas.grid(row=7, column=1, pady=5)

    # Personajes
    tk.Label(
        ventana,
        text="Personajes requeridos:"
    ).grid(row=8, column=0, sticky="w", padx=20, pady=5)

    personajes = tk.Entry(ventana, width=40)
    personajes.grid(row=8, column=1, pady=5)

    # Equipo técnico
    tk.Label(
        ventana,
        text="Equipo técnico asignado:"
    ).grid(row=9, column=0, sticky="w", padx=20, pady=5)

    equipo = tk.Entry(ventana, width=40)
    equipo.grid(row=9, column=1, pady=5)

    # Equipamiento
    tk.Label(
        ventana,
        text="Equipamiento necesario:"
    ).grid(row=10, column=0, sticky="w", padx=20, pady=5)

    equipamiento = tk.Entry(ventana, width=40)
    equipamiento.grid(row=10, column=1, pady=5)

    # Requerimientos especiales
    tk.Label(
        ventana,
        text="Requerimientos especiales:"
    ).grid(row=11, column=0, sticky="w", padx=20, pady=5)

    requerimientos = tk.Entry(ventana, width=40)
    requerimientos.grid(row=11, column=1, pady=5)

    # Plan de contingencia
    tk.Label(
        ventana,
        text="Plan de contingencia:"
    ).grid(row=12, column=0, sticky="w", padx=20, pady=5)

    contingencia = tk.Entry(ventana, width=40)
    contingencia.grid(row=12, column=1, pady=5)


    # --------------------------------------------------------
    # FUNCIÓN REGISTRAR
    # --------------------------------------------------------

    def registrar():

        if codigo.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el código de producción."
            )

        elif fecha.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar la fecha."
            )

        elif localizacion.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar la localización."
            )

        else:
            messagebox.showinfo(
                "Registro",
                "El plan de rodaje fue registrado correctamente."
            )


    # --------------------------------------------------------
    # FUNCIÓN LIMPIAR
    # --------------------------------------------------------

    def limpiar():

        codigo.delete(0, tk.END)
        dia.delete(0, tk.END)
        fecha.delete(0, tk.END)
        inicio.delete(0, tk.END)
        fin.delete(0, tk.END)
        localizacion.delete(0, tk.END)
        escenas.delete(0, tk.END)
        personajes.delete(0, tk.END)
        equipo.delete(0, tk.END)
        equipamiento.delete(0, tk.END)
        requerimientos.delete(0, tk.END)
        contingencia.delete(0, tk.END)


    # --------------------------------------------------------
    # BOTONES
    # --------------------------------------------------------

    tk.Button(
        ventana,
        text="Registrar",
        command=registrar,
        bg="#65B891",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).grid(row=13, column=0, pady=20)

    tk.Button(
        ventana,
        text="Limpiar",
        command=limpiar,
        bg="#8E7CC3",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).grid(row=13, column=1, pady=20)