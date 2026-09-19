import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def crear_personal(ventana):

    tk.Label(
        ventana,
        text="PERSONAL CREATIVO Y TÉCNICO",
        font=("Arial", 16, "bold"),
        fg="#6A4C93"
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=15
    )

    # Código
    tk.Label(
        ventana,
        text="Código:"
    ).grid(row=1, column=0, sticky="w", padx=20, pady=5)

    codigo = tk.Entry(ventana, width=40)
    codigo.grid(row=1, column=1, pady=5)

    # Nombres
    tk.Label(
        ventana,
        text="Nombres:"
    ).grid(row=2, column=0, sticky="w", padx=20, pady=5)

    nombres = tk.Entry(ventana, width=40)
    nombres.grid(row=2, column=1, pady=5)

    # Apellidos
    tk.Label(
        ventana,
        text="Apellidos:"
    ).grid(row=3, column=0, sticky="w", padx=20, pady=5)

    apellidos = tk.Entry(ventana, width=40)
    apellidos.grid(row=3, column=1, pady=5)

    # Especialidad
    tk.Label(
        ventana,
        text="Especialidad:"
    ).grid(row=4, column=0, sticky="w", padx=20, pady=5)

    especialidad = ttk.Combobox(
        ventana,
        values=[
            "Dirección",
            "Fotografía",
            "Sonido",
            "Edición",
            "Arte"
        ],
        width=37
    )

    especialidad.grid(row=4, column=1, pady=5)

    # Experiencia
    tk.Label(
        ventana,
        text="Experiencia previa:"
    ).grid(row=5, column=0, sticky="w", padx=20, pady=5)

    experiencia = tk.Entry(ventana, width=40)
    experiencia.grid(row=5, column=1, pady=5)

    # Portfolio
    tk.Label(
        ventana,
        text="Portfolio:"
    ).grid(row=6, column=0, sticky="w", padx=20, pady=5)

    portfolio = tk.Entry(ventana, width=40)
    portfolio.grid(row=6, column=1, pady=5)

    # Disponibilidad
    tk.Label(
        ventana,
        text="Disponibilidad:"
    ).grid(row=7, column=0, sticky="w", padx=20, pady=5)

    disponibilidad = ttk.Combobox(
        ventana,
        values=[
            "Disponible",
            "No disponible"
        ],
        width=37
    )

    disponibilidad.grid(row=7, column=1, pady=5)

    # Tarifa diaria
    tk.Label(
        ventana,
        text="Tarifa diaria:"
    ).grid(row=8, column=0, sticky="w", padx=20, pady=5)

    tarifa_diaria = tk.Entry(ventana, width=40)
    tarifa_diaria.grid(row=8, column=1, pady=5)

    # Tarifa semanal
    tk.Label(
        ventana,
        text="Tarifa semanal:"
    ).grid(row=9, column=0, sticky="w", padx=20, pady=5)

    tarifa_semanal = tk.Entry(ventana, width=40)
    tarifa_semanal.grid(row=9, column=1, pady=5)

    # Contacto
    tk.Label(
        ventana,
        text="Contacto:"
    ).grid(row=10, column=0, sticky="w", padx=20, pady=5)

    contacto = tk.Entry(ventana, width=40)
    contacto.grid(row=10, column=1, pady=5)

    # Producciones asignadas
    tk.Label(
        ventana,
        text="Producciones asignadas:"
    ).grid(row=11, column=0, sticky="w", padx=20, pady=5)

    producciones = tk.Entry(ventana, width=40)
    producciones.grid(row=11, column=1, pady=5)


    # --------------------------------------------------------
    # FUNCIÓN REGISTRAR
    # --------------------------------------------------------

    def registrar():

        if codigo.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el código."
            )

        elif nombres.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar los nombres."
            )

        elif apellidos.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar los apellidos."
            )

        else:
            messagebox.showinfo(
                "Registro",
                "Los datos del personal fueron registrados correctamente."
            )


    # --------------------------------------------------------
    # FUNCIÓN LIMPIAR
    # --------------------------------------------------------

    def limpiar():

        codigo.delete(0, tk.END)
        nombres.delete(0, tk.END)
        apellidos.delete(0, tk.END)
        experiencia.delete(0, tk.END)
        portfolio.delete(0, tk.END)
        tarifa_diaria.delete(0, tk.END)
        tarifa_semanal.delete(0, tk.END)
        contacto.delete(0, tk.END)
        producciones.delete(0, tk.END)

        especialidad.set("")
        disponibilidad.set("")


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
    ).grid(row=12, column=0, pady=20)

    tk.Button(
        ventana,
        text="Limpiar",
        command=limpiar,
        bg="#8E7CC3",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).grid(row=12, column=1, pady=20)