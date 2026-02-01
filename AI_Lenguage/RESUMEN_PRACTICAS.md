# Resumen de Prácticas - Azure AI-102: Language Services

Este directorio contiene prácticas de formación para la certificación **Azure AI-102**, enfocadas en el uso de **Azure AI Language Services** a través del SDK de Python.

## Estructura de Archivos

### 📋 AzureAI.txt
Archivo de configuración y requisitos que explica:
- Requisitos previos para uso de los scripts.
- Configuración de variables de entorno necesarias para autenticación:
  - `LANGUAGE_KEY`: Clave de acceso API.
  - `LANGUAGE_ENDPOINT`: URL del endpoint del servicio.
- Instalación de dependencias requeridas (`azure-ai-textanalytics==5.2.0`).

**Nota**: Este archivo debe ser referenciado antes de ejecutar cualquier script de Python en esta carpeta.

---

## 🐍 Scripts de Python

### Deteccion_Idioma.py
**Propósito**: Detectar el idioma de un texto dado.

**Funcionalidad**:
- Autentica el cliente utilizando credenciales de Azure.
- Realiza análisis de detección de idiomas.
- Identifica el idioma principal del documento.
- Soporta hint de país (`country_hint` = 'es' para español).

**Entrada**: Texto o lista de documentos.
**Salida**: Idioma detectado y su nombre.

**Código de ejemplo**:
```python
documents = ["Hi, whats your name? Las palabras."]
response = client.detect_language(documents = documents, country_hint = 'es')[0]
print("Language: ", response.primary_language.name)
```

---

### Extraccion_frases_clave.py
**Propósito**: Extraer frases clave (key phrases) de documentos.

**Funcionalidad**:
- Autentica el cliente utilizando credenciales de Azure.
- Realiza análisis de extracción de frases clave.
- Identifica los términos más importantes de un documento.
- Útil para resumen automático y análisis de contenido.

**Entrada**: Ruta de archivo o texto.
**Salida**: Lista de frases clave encontradas en el documento.

**Código de ejemplo**:
```python
documents = ['El servicio del personal fue bueno, el televisor de la habitación no funcionaba. En general, la limpieza del hotel es de buena calidad.']
response = client.extract_key_phrases(documents = documents)[0]
# Itera sobre las frases clave encontradas
for phrase in response.key_phrases:
    print(phrase)
```

---

## ⚙️ Configuración Requerida

Antes de ejecutar cualquier script de Python, asegúrate de:

1. **Crear un servicio de Azure Language**:
   - Accede a [Azure Portal](https://portal.azure.com/#home)
   - Crea un nuevo recurso de "Azure AI Language"

2. **Establecer variables de entorno**:
   ```bash
   export LANGUAGE_KEY=your-key
   export LANGUAGE_ENDPOINT=your-endpoint
   ```

3. **Instalar dependencias**:
   ```bash
   pip install azure-ai-textanalytics==5.2.0
   ```

---

## 📚 Referencia

- **Certificación**: Azure AI-102.
- **Servicio**: Azure AI Language Services.
- **SDK**: Azure AI Text Analytics for Python.
- **Documentación**: SDK de Foundry (Microsoft Azure).

---

## 🔗 Capacidades de Azure Language

Estas prácticas cubren dos de las muchas capacidades disponibles:
- ✅ **Detección de idiomas**: Identificar idiomas en textos.
- ✅ **Extracción de frases clave**: Identificar términos importantes.
- ❌ (No implementado) Análisis de sentimiento.
- ❌ (No implementado) Reconocimiento de entidades nombradas.
- ❌ (No implementado) Análisis de componentes clave.

