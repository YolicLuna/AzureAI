# Prácticas en Azure AI 🚀

Repositorio de proyectos y prácticas para aprender Azure AI. Este espacio documenta mi progreso hacia una comprensión más profunda de las capacidades de inteligencia artificial en Microsoft Azure.

## Contenido del Repositorio

### 📁 Proyectos Completados

#### 1. **Crear_Agentes**
Primer proyecto práctico implementando agentes de IA usando **Azure AI Foundry**.

**Descripción:**
- Creación de un agente de IA que resuelve problemas matemáticos
- Utiliza la herramienta **CodeInterpreterTool** para ejecutar código y cálculos
- Implementa un flujo de conversación con hilos (threads) para interacción usuario-agente
- Demuestra autenticación con Azure mediante `DefaultAzureCredential`

**Características principales:**
- ✅ Creación dinámica de agentes
- ✅ Procesamiento de mensajes en hilos de conversación
- ✅ Ejecución de instrucciones adicionales en runtime
- ✅ Gestión de recursos (eliminación de agentes)

**Estructura:**
```
Crear_Agentes/
├── agente.py              # Script principal del agente
├── requirements.txt       # Dependencias del proyecto
└── .env                   # Variables de entorno (ver configuración abajo)
```

**Requisitos:**
- Python 3.8+
- Cuenta en Microsoft Foundry (Azure AI)
- Credenciales de Azure configuradas

**Instalación:**
1. Instala las dependencias:
   ```bash
   pip install -r Crear_Agentes/requirements.txt
   ```

2. Configura el archivo `.env`:
   ```
   Foundry_endpoint='Coloca aquí tu endpoint del proyecto creado en Microsoft Foundry'
   Deployment_model='Coloca aquí el nombre del modelo que creaste y desplegaste en Microsoft Foundry'
   ```

3. Ejecuta el script:
   ```bash
   python Crear_Agentes/agente.py
   ```

---

#### 2. **Computer_vision**
Segundo proyecto práctico implementando análisis de imágenes usando **Azure Computer Vision API**.

**Descripción:**
- Análisis automatizado de imágenes utilizando Azure AI Vision
- Extrae información detallada: captions, etiquetas, objetos y detección de personas
- Anotación visual de objetos y personas detectadas en las imágenes
- Procesamiento de múltiples imágenes con parámetros dinámicos

**Características principales:**
- ✅ Análisis de captions (descripciones breves)
- ✅ Dense captions (descripciones detalladas de múltiples regiones)
- ✅ Generación automática de etiquetas (tags)
- ✅ Detección y anotación de objetos
- ✅ Detección y anotación de personas
- ✅ Exportación de imágenes con cuadros delimitadores

**Estructura:**
```
Computer_vision/
├── Analisis_de_Imagenes.py     # Script principal de análisis
├── Respuestas_obtenidas.md     # Documento con resultados del análisis
├── requirements.txt             # Dependencias del proyecto
├── .env                         # Variables de entorno (ver configuración abajo)
├── images/                      # Carpeta con imágenes a analizar
└── Imagenes_analisis/           # Carpeta con imágenes anotadas (resultados)
```

**Requisitos:**
- Python 3.8+
- Servicio Azure Computer Vision previamente creado
- Credenciales de Azure (endpoint y API key)

**Instalación:**
1. Instala las dependencias:
   ```bash
   pip install -r Computer_vision/requirements.txt
   ```

2. Configura el archivo `.env`:
   ```
   AI_SERVICE_ENDPOINT='Aquí coloca el endpoint de tu Computer Vision creado en Microsoft Azure'
   AI_SERVICE_KEY='Aquí coloca la API key de tu Computer Vision creado en Microsoft Azure'
   ```

3. Prepara tus imágenes en la carpeta `Computer_vision/images/`

4. Ejecuta el script:
   ```bash
   python Computer_vision/Analisis_de_Imagenes.py images/nombre_imagen.jpg
   ```

5. Consulta los resultados del análisis en [Respuestas_obtenidas.md](Computer_vision/Respuestas_obtenidas.md)

---

#### 3. **AI_Lenguage**
Tercer proyecto práctico enfocado en **Azure AI Language Services** para procesamiento de texto natural.

**Descripción:**
- Prácticas de formación para la certificación **Azure AI-102**
- Análisis de texto utilizando Azure AI Language Services
- Detección automática de idiomas en documentos
- Extracción de frases clave para análisis de contenido

**Características principales:**
- ✅ Detección de idiomas con hint de país
- ✅ Extracción de frases clave
- ✅ Autenticación con Azure mediante credenciales

**Estructura:**
```
AI_Lenguage/
├── Deteccion_Idioma.py          # Script de detección de idiomas
├── Extraccion_frases_clave.py   # Script de extracción de frases clave
├── AzureAI.txt                  # Guía de configuración y requisitos
├── RESUMEN_PRACTICAS.md         # Documentación detallada de las prácticas
└── .env                         # Variables de entorno (ver configuración abajo)
```

**Requisitos:**
- Python 3.8+
- Servicio Azure AI Language previamente creado
- Credenciales de Azure (endpoint y API key)

**Instalación:**
1. Instala las dependencias:
   ```bash
   pip install azure-ai-textanalytics==5.2.0
   ```

2. Configura las variables de entorno:
   ```bash
   export LANGUAGE_KEY='your-key'
   export LANGUAGE_ENDPOINT='your-endpoint'
   ```

3. Ejecuta los scripts:
   ```bash
   # Detección de idiomas
   python AI_Lenguage/Deteccion_Idioma.py
   
   # Extracción de frases clave
   python AI_Lenguage/Extraccion_frases_clave.py
   ```

Para más detalles, consulta [RESUMEN_PRACTICAS.md](AI_Lenguage/RESUMEN_PRACTICAS.md).

---

### 📚 Configuración General

#### Instalación de Azure CLI (Ubuntu 24.04)
Se proporciona una guía completa en [Instalar_AzureCLI.md](Instalar_AzureCLI.md) para configurar Azure CLI en sistemas Ubuntu/Debian.

---

## ⚙️ Requisitos Previos Importantes

**Antes de ejecutar cualquier proyecto en este repositorio, debes:**
1. Crear los servicios necesarios en **Microsoft Azure** o **Microsoft Foundry**
2. Obtener las credenciales correspondientes (endpoints, API keys, etc.)
3. Configurar el archivo `.env` con esas credenciales
4. **Los proyectos aquí documentados NO incluyen instrucciones para crear los servicios en Azure**

Cada proyecto especifica qué servicio de Azure se requiere. Consulta la [documentación oficial de Microsoft](https://learn.microsoft.com/es-es/azure/ai/) para crear los servicios necesarios.

---

## 🔐 Notas de Seguridad

- Los archivos `.env` contienen variables de entorno sensibles y **no deben ser compartidos en repositorios públicos**
- En este repositorio, las credenciales han sido reemplazadas por instrucciones para mayor claridad
- Los recursos de prueba fueron eliminados después de validar que código en funcionara
---

## 📖 Recursos de Aprendizaje

- [Documentación oficial de Azure AI](https://learn.microsoft.com/es-es/azure/ai/)
- [Azure AI Agents Framework](https://learn.microsoft.com/es-es/azure/ai-studio/how-to/agents)
- [Certificación AI-900](https://learn.microsoft.com/es-es/credentials/certifications/azure-ai-fundamentals/)
- [Certificación AI-102](https://learn.microsoft.com/es-es/credentials/certifications/azure-ai-engineer/)
- [Bootcamp Azure AI Engineer Associate](https://codigofacilito.com/programas/ai102-g5)

---

## 📝 Notas

Este repositorio refleja un proceso de aprendizaje continuo. Cada proyecto incluye comentarios detallados y se actualiza con nuevas prácticas conforme progreso en Azure AI.

---

**Última actualización:** 16 de enero de 2026
