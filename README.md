# Azure AI - Prácticas para Certificación AI-102

Este repositorio contiene una colección de prácticas y ejercicios realizados como parte de la preparación para el examen de certificación **Microsoft Azure AI Engineer (AI-102)**.

## 📚 Descripción

Durante la preparación para obtener la certificación AI-102, se llevaron a cabo prácticas enfocadas en diferentes servicios de Azure AI. La mayoría del código fue adquirido a través de módulos de **Microsoft Learn**, donde se proporcionaban ejercicios guiados que fueron replicados y adaptados para profundizar en los conceptos de Inteligencia Artificial en Azure.

---

## 📁 Estructura del Proyecto

El proyecto está organizado en cuatro carpetas principales, cada una enfocada en un aspecto diferente de Azure AI:

### 1. **AI_Lenguage** - Procesamiento de Lenguaje Natural
**Ubicación:** `AI_Lenguage/`

Prácticas relacionadas con el servicio **Azure AI Language** para procesar y analizar texto:

- **Deteccion_Idioma.py**: Detecta automáticamente el idioma de un texto usando `TextAnalyticsClient`
  - Utiliza el parámetro `country_hint` para mejorar la precisión
  - Retorna el nombre del idioma detectado con su confianza

- **Extraccion_frases_clave.py**: Extrae frases clave de un texto en español
  - Analiza documentos para identificar términos relevantes
  - Útil para búsqueda, categorización y análisis de sentimientos avanzados
  - Retorna las frases clave identificadas

**Requisitos:**
```bash
pip install azure-ai-textanalytics==5.2.0
```

**Configuración:** Se requieren variables de entorno:
```bash
export LANGUAGE_KEY=your-key
export LANGUAGE_ENDPOINT=your-endpoint
```

---

### 2. **Computer_Vision** - Análisis de Imágenes
**Ubicación:** `Computer_vision/`

Prácticas con el servicio **Azure AI Vision** para análisis avanzado de imágenes:

- **Analisis_de_Imagenes.py**: Realiza un análisis completo de imágenes con múltiples características:
  - **Captions**: Genera descripciones automáticas de la imagen
  - **Dense Captions**: Proporciona descripciones detalladas de diferentes regiones
  - **Tags**: Identifica etiquetas y categorías de la imagen
  - **Objects**: Detecta objetos específicos y su ubicación
  - **People**: Identifica personas y sus ubicaciones en la imagen
  - Visualiza los resultados con bounding boxes usando `matplotlib` y `PIL`

**Requisitos:**
```bash
pip install -r requirements.txt
```

Que incluye:
- `python-dotenv`: Manejo de variables de entorno
- `Pillow`: Procesamiento de imágenes
- `matplotlib`: Visualización de gráficos
- `azure-core`: Autenticación y comunicación
- `azure-ai-vision`: Cliente de Azure Vision
- `requests`: Solicitudes HTTP

---

### 3. **Content_Understanding** - Análisis de Documentos
**Ubicación:** `Content_Understanding/analisis_documentto/`

Prácticas con **Azure Document Intelligence** (anteriormente Form Recognizer) para extracción de información de documentos:

- **document-analysis.py**: Analiza documentos (facturas, recibos, etc.) usando modelos preentrenados
  - Utiliza el modelo `prebuilt-invoice` para análisis de facturas
  - Extrae campos específicos como:
    - Nombre del vendedor
    - Nombre del cliente
    - Monto total de la factura
  - Retorna valores con niveles de confianza
  - Soporta análisis de documentos desde URL

**Requisitos:**
```bash
pip install -r requirements.txt
```

Que incluye:
- `python-dotenv`: Manejo de variables de entorno
- `azure-ai-formrecognizer==3.3.3`: Cliente de Document Intelligence
- `azure-core>=1.26.0`: Autenticación y comunicación

**Posibles Mejoras:**
- Analizar otros tipos de documentos (recibos, tarjetas de identificación, etc.)
- Procesamiento por lotes de múltiples documentos
- Entrenamiento de modelos personalizados

---

### 4. **Crear_Agentes** - Agentes de IA Conversacionales
**Ubicación:** `Crear_Agentes/`

Prácticas con **Agents en Azure AI Foundry** para crear agentes de IA conversacionales:

- **agente.py**: Crea un agente de IA con capacidades avanzadas:
  - Utiliza el servicio **Azure AI Projects** para gestionar agentes
  - Integra la herramienta **Code Interpreter** para ejecutar código Python
  - Implementa un sistema de hilos de conversación (threads)
  - El agente puede responder preguntas matemáticas usando código
  - Demuestra el ciclo completo: crear agente → crear hilo → enviar mensaje → procesar respuesta

**Requisitos:**
```bash
pip install -r requirements.txt
```

Que incluye:
- `azure-ai-projects`: Cliente para gestionar proyectos de IA
- `azure-identity`: Autenticación con Azure
- `python-dotenv`: Manejo de variables de entorno

**Configuración:** Se requieren variables de entorno:
```bash
Foundry_endpoint=your-endpoint
Deployment_model=your-model
```

---

## 🛠️ Configuración General

### Requisitos Previos
- Python 3.7 o superior
- Una cuenta de Microsoft Azure activa
- Credenciales de acceso a los servicios de Azure AI

### Entorno Virtual
Se incluye un entorno virtual de Python (`labenv/`) que contiene todas las dependencias necesarias. Para usar el proyecto:

1. **Activar el entorno virtual:**
   - En Windows: `labenv\Scripts\activate.bat`
   - En macOS/Linux: `source labenv/bin/activate`

2. **Verificar instalación de paquetes:**
   ```bash
   pip list
   ```

3. **Instalar dependencias adicionales si es necesario:**
   ```bash
   pip install -r [ruta-a-requirements.txt]
   ```

### Variables de Entorno
Cada módulo requiere variables de entorno específicas. Se recomienda:

1. Crear un archivo `.env` en la raíz del proyecto
2. O en carpetas específicas con un archivo `env.txt`
3. Los archivos de variables sensibles están incluidos en `.gitignore`

---

## 📖 Fuentes y Referencias

Todas las prácticas están basadas en módulos oficiales de **Microsoft Learn**:

- [Azure AI Language](https://learn.microsoft.com/es-es/training/modules/analyze-text-with-text-analytics-service/)
- [Azure AI Vision](https://learn.microsoft.com/es-es/training/modules/analyze-images-computer-vision/)
- [Document Intelligence](https://learn.microsoft.com/es-es/training/modules/extract-data-from-forms/)
- [Azure AI Agents](https://learn.microsoft.com/es-es/training/modules/build-agents-azure-ai/)

---

## ✅ Aprendizajes Clave

A través de estas prácticas se han adquirido competencias en:

1. **Procesamiento de Lenguaje Natural (NLP)**
   - Detección de idiomas multilingües
   - Extracción de términos relevantes
   - Comprensión del texto

2. **Visión por Computadora**
   - Análisis de contenido de imágenes
   - Detección de objetos y personas
   - Generación de descripciones automáticas

3. **Extracción de Información de Documentos**
   - Análisis de documentos estructurados
   - Extracción de datos específicos
   - Modelos preentrenados de Azure

4. **Agentes de IA Conversacionales**
   - Creación y gestión de agentes
   - Integración de herramientas (Code Interpreter)
   - Gestión de conversaciones con threads

5. **Buenas Prácticas en Azure**
   - Autenticación y seguridad
   - Manejo de variables de entorno
   - Gestión de recursos y limpieza

---

## 📝 Notas Importantes

- Los recursos de Azure utilizados en cada práctica fueron eliminados después de completar el ejercicio para evitar cargos innecesarios
- Algunos documentos de prueba pueden no estar disponibles (URL externas)
- El código está comentado en español para mejor comprensión
- Se recomienda seguir los módulos de Microsoft Learn para una comprensión profunda de cada tema

---

## 🎯 Próximos Pasos

Para continuar profundizando en Azure AI:

- Explorar análisis de sentimientos con Text Analytics
- Implementar traducción automática de textos
- Crear modelos de clasificación personalizados
- Desarrollar soluciones end-to-end combinando múltiples servicios
- Preparar y presentar el examen AI-102

---

**Última actualización:** Marzo 2026  
**Certificación objetivo:** Microsoft Azure AI Engineer (AI-102)
