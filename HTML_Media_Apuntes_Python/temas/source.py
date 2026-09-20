TITULO = "HTML <source>"

def mostrar():
    print('''
<source>
========

Permite proporcionar varias fuentes alternativas para <audio>
o <video>.

Ejemplo:
<video controls>
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
</video>

¿POR QUÉ?
Los navegadores pueden tener diferente soporte de formatos.

También se utiliza con <picture> para imágenes adaptables.

IMPORTANTE:
<source> es un elemento vacío: no necesita </source>.
''')

if __name__ == "__main__":
    mostrar()
