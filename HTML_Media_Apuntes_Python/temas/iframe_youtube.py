TITULO = "HTML <iframe> y YouTube"

def mostrar():
    print('''
<iframe>
========

Permite insertar otro documento o servicio web dentro de una página.

Ejemplo de YouTube:
<iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/ID_DEL_VIDEO"
    title="Video de YouTube"
    allowfullscreen>
</iframe>

¿CUÁNDO USARLO?
Cuando el contenido está alojado en YouTube u otro servicio
externo que ofrece una URL de inserción.

DIFERENCIA:
<video> -> reproduce un archivo de video que controlas.
<iframe> -> inserta otro documento/servicio.

Para contenido externo también existen medidas de seguridad
como el atributo sandbox.
''')

if __name__ == "__main__":
    mostrar()
