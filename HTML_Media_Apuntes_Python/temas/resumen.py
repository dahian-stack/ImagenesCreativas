TITULO = "Resumen — Recomendado vs. antiguo"

def mostrar():
    print('''
RESUMEN
=======

<audio>   -> audio HTML.
<video>   -> video HTML.
<source>  -> fuentes alternativas.
<iframe>  -> otra página/servicio, como YouTube.
<object>  -> recursos externos en casos específicos.
<embed>   -> recursos externos en casos específicos.

PARA RECORDAR:
AUDIO        -> <audio>
VIDEO        -> <video>
VARIOS FORMATOS -> <source>
YOUTUBE      -> <iframe>

TECNOLOGÍAS ANTIGUAS:
Flash, Java Applets y ActiveX dependían de plugins de navegador
que los navegadores modernos dejaron de admitir.

Por eso no se deben presentar como soluciones actuales.

FUENTES:
W3Schools y MDN Web Docs.
''')

if __name__ == "__main__":
    mostrar()
