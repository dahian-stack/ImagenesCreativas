TITULO = "HTML Audio — <audio>"

def mostrar():
    print('''
<audio>
========

Sirve para reproducir sonido en una página.

Ejemplo:
<audio controls>
    <source src="musica.mp3" type="audio/mpeg">
    <source src="musica.ogg" type="audio/ogg">
</audio>

ATRIBUTOS:
controls -> controles de reproducción.
autoplay -> intenta iniciar automáticamente.
muted -> inicia sin sonido.
loop -> repite el audio.

FORMATOS COMUNES:
MP3 -> audio/mpeg
WAV -> audio/wav
Ogg -> audio/ogg

RECOMENDACIÓN:
Para audio normal, usar <audio> en lugar de plugins antiguos.
''')

if __name__ == "__main__":
    mostrar()
