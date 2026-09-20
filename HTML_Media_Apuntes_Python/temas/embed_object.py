TITULO = "HTML <embed> y <object>"

def mostrar():
    print('''
<embed> Y <object>
==================

Sirven para incrustar determinados recursos externos.

<embed src="archivo.pdf" type="application/pdf">

<object data="archivo.pdf" type="application/pdf">
    Contenido alternativo.
</object>

IMPORTANTE:
Los elementos <embed> y <object> todavía existen en HTML y pueden
tener usos concretos. Lo que quedó obsoleto fue el antiguo modelo
de plugins de navegador como Flash, Java Applets y ActiveX.

W3Schools indica que los navegadores modernos ya no soportan esos
plugins antiguos.

PARA MULTIMEDIA:
Video propio -> <video>
Audio propio -> <audio>
YouTube -> <iframe>

No conviene usar <embed> para reemplazar <video> o <audio>.
''')

if __name__ == "__main__":
    mostrar()
