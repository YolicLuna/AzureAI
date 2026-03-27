import json

# Cargar JSON
with open("VideoTexto.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Ruta al OCR
ocr_data = data["videos"][0]["insights"]["ocr"]

# Extraer textos
textos = [item["text"] for item in ocr_data]

# Quitar duplicados manteniendo orden
texto_unico = list(dict.fromkeys(textos))

# Unir en un solo texto
texto_final = " ".join(texto_unico)

# Mostrar resultado
print("\nTEXTO FINAL:\n")
print(texto_final)

with open("texto_limpio.txt", "w", encoding="utf-8") as f:
    f.write(texto_final)

print("Texto guardado en texto_limpio.txt")