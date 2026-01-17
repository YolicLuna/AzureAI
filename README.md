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

### 📚 Configuración General

#### Instalación de Azure CLI (Ubuntu 24.04)
Se proporciona una guía completa en [Instalar_AzureCLI.md](Instalar_AzureCLI.md) para configurar Azure CLI en sistemas Ubuntu/Debian.

---

## 🔐 Notas de Seguridad

- Los archivos `.env` contienen variables de entorno sensibles y **no deben ser compartidos en repositorios públicos**
- En este repositorio, las credenciales han sido reemplazadas por instrucciones para mayor claridad
- Los recursos de prueba fueron eliminados después de validar el código en Microsoft Foundry

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
