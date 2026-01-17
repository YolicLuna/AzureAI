# Se importan las librerías necesarias.
# os para manejar variables de entorno.
# dotenv para cargar las variables de entorno desde un archivo .env.
# AIProjectClient para interactuar con el servicio de proyectos de IA de Azure.
# DefaultAzureCredential para la autenticación con Azure.
# CodeInterpreterTool para utilizar la herramienta de interpretación de código en el agente.

import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import CodeInterpreterTool

# Se cargan las variables de entorno desde el archivo .env.
# Se crea una instancia del cliente del proyecto de IA utilizando las credenciales predeterminadas de Azure.

load_dotenv()
project_client = AIProjectClient(
    endpoint=os.getenv('Foundry_endpoint'),
    credential=DefaultAzureCredential(),
)

# Se crea una instancia de la herramienta de interpretación de código.

code_interpreter = CodeInterpreterTool()

# Se utiliza un bloque 'with' para asegurar que el cliente del proyecto se cierre correctamente después de su uso.

with project_client:

    # Se crea un agente con instrucciones específicas y la herramienta de interpretación de código.
    agent = project_client.agents.create_agent(
        model=os.getenv('Deployment_model'),
        name = 'Mi agente',
        instructions = 'Responde adecuadamente y educadamente las preguntas de matematicas. Usa la herramienta de Code Interpreter cuando se visualicen numeros.',
        tools=code_interpreter.definitions,
    )
    print(f'Agente creado, ID: {agent.id}')

    # Se crea un hilo de conversación para el agente.
    thread = project_client.agents.threads.create()
    print(f'Hilo creado, ID: {thread.id}')
    
    # Se crea un mensaje de usuario en el hilo de conversación.
    message = project_client.agents.messages.create(
        thread_id = thread.id,
        role = 'user',
        content = '¿Cuanto es 1234 por 54789?'
    )
    print(f'Mensaje creado, ID: {message.id}')

    # Se crea y procesa una ejecución del agente en el hilo de conversación con instrucciones adicionales.
    run = project_client.agents.runs.create_and_process(
        thread_id=thread.id,
        agent_id=agent.id,
        instructions='Dirigete al usuario como un alumno de universidad.'
    )

    print(f'Ejecucion finalizada con estado, ID: {run.id}')

    # Si la ejecución falla, se imprime el error.
    if run.status == 'failed':
        print(f'Run failed: {run.last_error}')
    
    # Se listan y muestran todos los mensajes en el hilo de conversación.
    messages = project_client.agents.messages.list(thread_id=thread.id)
    for message in messages:
        print(f'Role: {message.role}, Content: {message.content}')
    
    # Se elimina el agente creado para limpiar recursos.
    project_client.agents.delete_agent(agent_id=agent.id)
    print('Agente eliminado')


'''
Respuestas que se esperan al ejecutar el código anterior:

Agente creado, ID: asst_VbdBag1lvjjVUiJ2V8fAoQxq
Hilo creado, ID: thread_HYHi9kRVBxKGMM348q01u5lG
Mensaje creado, ID: msg_1us947HcV5APyZ115RSZPgAr
Ejecucion finalizada con estado, ID: run_9ejanFVpYtuhYIIfgNoqdNyo
Role: MessageRole.AGENT, Content: [{'type': 'text', 'text': {'value': 'El resultado de multiplicar 1234 por 54789 es 67,609,626.', 'annotations': []}}]
Role: MessageRole.USER, Content: [{'type': 'text', 'text': {'value': '¿Cuanto es 1234 por 54789?', 'annotations': []}}]
Agente eliminado
''' 