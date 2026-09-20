TITULO = "HTML Video — <video>"

def mostrar():
    print('''
<video>
========

Sirve para reproducir videos directamente en HTML.

Ejemplo:
<video controls width="640">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    Tu navegador no soporta el video.
</video>

ATRIBUTOS IMPORTANTES
controls -> muestra controles.
width/height -> dimensiones.
autoplay -> intenta reproducir automáticamente.
muted -> inicia sin sonido.
loop -> repite el video.
poster -> imagen de portada antes de reproducir.

RECOMENDACIÓN:
Usar <video> para videos que forman parte de la página.
También se pueden ofrecer varios <source>.
''')

if __name__ == "__main__":
    mostrar()
