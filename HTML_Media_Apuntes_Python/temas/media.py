TITULO = "HTML Media — Introducción"

def mostrar():
    print('''
HTML MEDIA
===========

HTML permite incorporar contenido multimedia como audio y video.

Ejemplo:
<video controls>
    <source src="video.mp4" type="video/mp4">
</video>

<video>  -> reproductor de video.
<audio>  -> reproductor de audio.
<source> -> archivo/fuente multimedia alternativa.

RECOMENDACIÓN:
Para audio y video modernos se utilizan las etiquetas nativas
<audio> y <video>; no hacen falta plugins externos.
''')

if __name__ == "__main__":
    mostrar()
