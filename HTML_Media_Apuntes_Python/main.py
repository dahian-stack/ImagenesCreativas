from temas import media, video, audio, source, iframe_youtube, embed_object, resumen

temas = [media, video, audio, source, iframe_youtube, embed_object, resumen]

print("=" * 55)
print("HTML MEDIA — APUNTES")
print("=" * 55)

for i, tema in enumerate(temas, 1):
    print(f"{i}. {tema.TITULO}")

opcion = input("\nElige un tema: ").strip()

if opcion.isdigit() and 1 <= int(opcion) <= len(temas):
    temas[int(opcion) - 1].mostrar()
else:
    print("Opción no válida.")
