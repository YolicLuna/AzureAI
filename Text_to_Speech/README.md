# Proyecto Text to Speech

## Descripción
Proyecto que convierte texto extraído de un video a audio mediante Azure Cognitive Services.

## Flujo del Proyecto

1. **Extracción de Texto (Video Indexer)**
   - Se utilizó Azure Video Indexer para analizar un video y extraer el texto mediante OCR
   - Se descargó el JSON con los insights (ocr data)

2. **Conversión JSON a TXT**
   - El script `extraccion_texto.py` procesa el JSON descargado
   - Extrae todos los textos del OCR, elimina duplicados manteniendo el orden
   - Genera el archivo `texto_limpio.txt`

3. **Corrección del Texto**
   - Se revisó y corrigió manualmente el `texto_limpio.txt` para solucionar errores de la detección de Video Indexer
   - El resultado se guardó en `texto_para_convertir.txt` (listo para síntesis de voz)

4. **Síntesis de Voz (Azure AI Services)**
   - Se creó un recurso de Azure Cognitive Services Speech
   - El script `text_speech.py` lee el texto corregido y lo convierte a audio MP3
   - Utiliza la voz neural `es-MX-DaliaNeural` (español de México natural)

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecución
```bash
python text_speech.py
```
