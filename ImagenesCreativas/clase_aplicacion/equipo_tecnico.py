import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def crear_equipos(ventana):

    tk.Label(
        ventana,
        text="EQUIPOS TÉCNICOS",
        font=("Arial", 16, "bold"),
        fg="#457B9D"
    ).grid(
        row=0,
        column=0,
        columnspan=2,
        pady=15
    )

    # Número de inventario
    tk.Label(
        ventana,
        text="Número de inventario:"
    ).grid(row=1, column=0, sticky="w", padx=20, pady=5)

    inventario = tk.Entry(ventana, width=40)
    inventario.grid(row=1, column=1, pady=5)

    # Categoría
    tk.Label(
        ventana,
        text="Categoría:"
    ).grid(row=2, column=0, sticky="w", padx=20, pady=5)

    categoria = ttk.Combobox(
        ventana,
        values=[
            "Cámara",
            "Iluminación",
            "Sonido",
            "Grip"
        ],
        width=37
    )

    categoria.grid(row=2, column=1, pady=5)

    # Marca
    tk.Label(
        ventana,
        text="Marca:"
    ).grid(row=3, column=0, sticky="w", padx=20, pady=5)

    marca = tk.Entry(ventana, width=40)
    marca.grid(row=3, column=1, pady=5)

    # Modelo
    tk.Label(
        ventana,
        text="Modelo:"
    ).grid(row=4, column=0, sticky="w", padx=20, pady=5)

    modelo = tk.Entry(ventana, width=40)
    modelo.grid(row=4, column=1, pady=5)

    # Características técnicas
    tk.Label(
        ventana,
        text="Características técnicas:"
    ).grid(row=5, column=0, sticky="w", padx=20, pady=5)

    caracteristicas = tk.Entry(ventana, width=40)
    caracteristicas.grid(row=5, column=1, pady=5)

    # Fecha de adquisición
    tk.Label(
        ventana,
        text="Fecha de adquisición:"
    ).grid(row=6, column=0, sticky="w", padx=20, pady=5)

    fecha = tk.Entry(ventana, width=40)
    fecha.grid(row=6, column=1, pady=5)

    # Valor
    tk.Label(
        ventana,
        text="Valor:"
    ).grid(row=7, column=0, sticky="w", padx=20, pady=5)

    valor = tk.Entry(ventana, width=40)
    valor.grid(row=7, column=1, pady=5)

    # Estado
    tk.Label(
        ventana,
        text="Estado:"
    ).grid(row=8, column=0, sticky="w", padx=20, pady=5)

    estado = ttk.Combobox(
        ventana,
        values=[
            "Disponible",
            "En mantenimiento",
            "Dañado"
        ],
        width=37
    )

    estado.grid(row=8, column=1, pady=5)

    # Disponibilidad
    tk.Label(
        ventana,
        text="Disponibilidad:"
    ).grid(row=9, column=0, sticky="w", padx=20, pady=5)

    disponibilidad = ttk.Combobox(
        ventana,
        values=[
            "Disponible",
            "No disponible"
        ],
        width=37
    )

    disponibilidad.grid(row=9, column=1, pady=5)

    # Seguro
    tk.Label(
        ventana,
        text="Seguro:"
    ).grid(row=10, column=0, sticky="w", padx=20, pady=5)

    seguro = ttk.Combobox(
        ventana,
        values=[
            "Sí",
            "No"
        ],
        width=37
    )

    seguro.grid(row=10, column=1, pady=5)

    # Mantenimientos
    tk.Label(
        ventana,
        text="Mantenimientos programados:"
    ).grid(row=11, column=0, sticky="w", padx=20, pady=5)

    mantenimientos = tk.Entry(ventana, width=40)
    mantenimientos.grid(row=11, column=1, pady=5)

    # Producciones asignadas
    tk.Label(
        ventana,
        text="Producciones asignadas:"
    ).grid(row=12, column=0, sticky="w", padx=20, pady=5)

    producciones = tk.Entry(ventana, width=40)
    producciones.grid(row=12, column=1, pady=5)


    # --------------------------------------------------------
    # FUNCIÓN REGISTRAR
    # --------------------------------------------------------

    def registrar():

        if inventario.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el número de inventario."
            )

        elif marca.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar la marca."
            )

        elif modelo.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el modelo."
            )

        else:
            messagebox.showinfo(
                "Registro",
                "El equipo fue registrado correctamente."
            )


    # --------------------------------------------------------
    # FUNCIÓN LIMPIAR
    # --------------------------------------------------------

    def limpiar():

        inventario.delete(0, tk.END)
        marca.delete(0, tk.END)
        modelo.delete(0, tk.END)
        caracteristicas.delete(0, tk.END)
        fecha.delete(0, tk.END)
        valor.delete(0, tk.END)
        mantenimientos.delete(0, tk.END)
        producciones.delete(0, tk.END)

        categoria.set("")
        estado.set("")
        disponibilidad.set("")
        seguro.set("")


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