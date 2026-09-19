import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def crear_localizaciones(ventana):

    tk.Label(
        ventana,
        text="LOCALIZACIONES",
        font=("Arial", 16, "bold"),
        fg="#E09F3E"
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

    # Nombre
    tk.Label(
        ventana,
        text="Nombre:"
    ).grid(row=2, column=0, sticky="w", padx=20, pady=5)

    nombre = tk.Entry(ventana, width=40)
    nombre.grid(row=2, column=1, pady=5)

    # Dirección
    tk.Label(
        ventana,
        text="Dirección:"
    ).grid(row=3, column=0, sticky="w", padx=20, pady=5)

    direccion = tk.Entry(ventana, width=40)
    direccion.grid(row=3, column=1, pady=5)

    # Coordenadas
    tk.Label(
        ventana,
        text="Coordenadas:"
    ).grid(row=4, column=0, sticky="w", padx=20, pady=5)

    coordenadas = tk.Entry(ventana, width=40)
    coordenadas.grid(row=4, column=1, pady=5)

    # Tipo
    tk.Label(
        ventana,
        text="Tipo:"
    ).grid(row=5, column=0, sticky="w", padx=20, pady=5)

    tipo = ttk.Combobox(
        ventana,
        values=[
            "Interior",
            "Exterior",
            "Estudio"
        ],
        width=37
    )

    tipo.grid(row=5, column=1, pady=5)

    # Propietario
    tk.Label(
        ventana,
        text="Propietario:"
    ).grid(row=6, column=0, sticky="w", padx=20, pady=5)

    propietario = tk.Entry(ventana, width=40)
    propietario.grid(row=6, column=1, pady=5)

    # Características relevantes
    tk.Label(
        ventana,
        text="Características relevantes:"
    ).grid(row=7, column=0, sticky="w", padx=20, pady=5)

    caracteristicas = tk.Entry(ventana, width=40)
    caracteristicas.grid(row=7, column=1, pady=5)

    # Permisos
    tk.Label(
        ventana,
        text="Permisos necesarios:"
    ).grid(row=8, column=0, sticky="w", padx=20, pady=5)

    permisos = tk.Entry(ventana, width=40)
    permisos.grid(row=8, column=1, pady=5)

    # Costo
    tk.Label(
        ventana,
        text="Costo:"
    ).grid(row=9, column=0, sticky="w", padx=20, pady=5)

    costo = tk.Entry(ventana, width=40)
    costo.grid(row=9, column=1, pady=5)

    # Limitaciones
    tk.Label(
        ventana,
        text="Limitaciones de uso:"
    ).grid(row=10, column=0, sticky="w", padx=20, pady=5)

    limitaciones = tk.Entry(ventana, width=40)
    limitaciones.grid(row=10, column=1, pady=5)

    # Facilidades
    tk.Label(
        ventana,
        text="Facilidades disponibles:"
    ).grid(row=11, column=0, sticky="w", padx=20, pady=5)

    facilidades = tk.Entry(ventana, width=40)
    facilidades.grid(row=11, column=1, pady=5)

    # Accesibilidad
    tk.Label(
        ventana,
        text="Accesibilidad:"
    ).grid(row=12, column=0, sticky="w", padx=20, pady=5)

    accesibilidad = ttk.Combobox(
        ventana,
        values=[
            "Accesible",
            "Accesibilidad limitada",
            "No accesible"
        ],
        width=37
    )

    accesibilidad.grid(row=12, column=1, pady=5)

    # Producciones previas
    tk.Label(
        ventana,
        text="Producciones previas:"
    ).grid(row=13, column=0, sticky="w", padx=20, pady=5)

    producciones = tk.Entry(ventana, width=40)
    producciones.grid(row=13, column=1, pady=5)


    # --------------------------------------------------------
    # FUNCIÓN REGISTRAR
    # --------------------------------------------------------

    def registrar():

        if codigo.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el código."
            )

        elif nombre.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar el nombre."
            )

        elif direccion.get() == "":
            messagebox.showerror(
                "Error",
                "Debe ingresar la dirección."
            )

        else:
            messagebox.showinfo(
                "Registro",
                "La localización fue registrada correctamente."
            )


    # --------------------------------------------------------
    # FUNCIÓN LIMPIAR
    # --------------------------------------------------------

    def limpiar():

        codigo.delete(0, tk.END)
        nombre.delete(0, tk.END)
        direccion.delete(0, tk.END)
        coordenadas.delete(0, tk.END)
        propietario.delete(0, tk.END)
        caracteristicas.delete(0, tk.END)
        permisos.delete(0, tk.END)
        costo.delete(0, tk.END)
        limitaciones.delete(0, tk.END)
        facilidades.delete(0, tk.END)
        producciones.delete(0, tk.END)

        tipo.set("")
        accesibilidad.set("")


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
    ).grid(row=14, column=0, pady=20)

    tk.Button(
        ventana,
        text="Limpiar",
        command=limpiar,
        bg="#8E7CC3",
        fg="white",
        font=("Arial", 10, "bold"),
        width=12
    ).grid(row=14, column=1, pady=20)