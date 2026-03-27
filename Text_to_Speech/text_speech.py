import azure.cognitiveservices.speech as speechsdk

# Configuración (reemplaza con tus datos)
speech_config = speechsdk.SpeechConfig(
    subscription="Coloca_tu_clave_aquí",
    region="eastus"
)

# Voz recomendada en español (muy natural)
speech_config.speech_synthesis_voice_name = "es-MX-DaliaNeural"

audio_config = speechsdk.audio.AudioOutputConfig(filename="audio_final.mp3")

# Leer texto desde archivo
with open("texto_para_convertir.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Crear sintetizador
synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Generar audio
synthesizer.speak_text_async(texto).get()

print("Audio generado: audio_final.mp3")