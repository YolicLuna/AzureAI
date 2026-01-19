# Se importan las librerias para el analisis de imagenes.
from dotenv import load_dotenv
import os
from PIL import  Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.core.exceptions import HttpResponseError
import requests

# Se importan las librerias de Azure AI Vision.
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Funcion principal para el analisis de imagenes.
def main():
    os.system('cls' if os.name=='nt' else 'clear')

    # Se cargan las variables de entorno.
    try:
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Se obtiene la imagen a analizar.
        image_file = 'images/Galaxia.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]

        # Se crea el cliente de analisis de imagenes.
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        # Se abre la imagen y se lee en bytes.
        with open(image_file, 'rb') as f:
            image_data = f.read()
        print(f'\nAnalyzing {image_file}\n')

        # Se realiza el analisis de la imagen.
        result = cv_client.analyze(
            image_data = image_data,
            visual_features = [
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE
            ],
        )

        # Bloque para analozar la descripción de la imagen.
        if result.caption is not None:
            print('\nCaption:')
            print('Caption: "{}" (confidence: {:.2f}%)'.format(result.caption.text, result.caption.confidence * 100))

        # Bloque para analizar las descripciones detalladas de la imagen.
        if result.dense_captions is not None:
            print('\nDense Captions:')
            for caption in result.dense_captions.list:
                print(' Caption: "{}" (confidence: {:.2f}%)'.format(caption.text, caption.confidence * 100))
        
        # Bloque para obtener las diferentes etiquetas que puede tener la imagen.
        if result.tags is not None:
            print('\nTags:')
            for tag in result.tags.list:
                print(' Tag: "{}" (confidence: {:.2f}%)'.format(tag.name, tag.confidence * 100))

        # Bloque para identificar los objetos dentro de la imagen.
        if result.objects is not None:
            print('\nObjects in image:')
            for detected_object in result.objects.list:
                print(' "{}" (confidence: {:.2f}%)'.format(detected_object.tags[0].name, detected_object.tags[0].confidence * 100))
            
            show_objects(image_file, result.objects.list)

        # Bloque para identificar personas dentro de la imagen.
        if result.people is not None:
            print('\nPeople in image:')
            for detected_person in result.people.list:
                if detected_person.confidence > 0.2:
                    print(' "{}" (confidence: {:.2f}%)'.format(detected_person.bounding_box, detected_person.confidence * 100))

            show_people(image_file, result.people.list)
    
    # Manejo de errores.
    except Exception as ex:
        print(ex)

# Función para mostrar los objetos detectados en la imagen.
def show_objects(image_filname, detected_objects):
    print('\nAnnotating objects...')

    # Se abre la imagen.
    image = Image.open(image_filname)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    # Se dibujan los cuadros alrededor de los objetos detectados.
    for detected_object in detected_objects:
        r = detected_object.bounding_box
        bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
        draw.rectangle(bounding_box, outline=color, width=3)
        plt.annotate(detected_object.tags[0].name, (r.x, r.y), backgroundcolor=color)

    # Se muestra y guarda la imagen anotada.
    plt.imshow(image)
    plt.tight_layout(pad=0)
    objectfile = 'Galaxia.jpg' # Esta parte se cambia segun la imagen que se analice, ya que es el nombre con el que se guarda el resultado.
    fig.savefig(objectfile)
    print('\nResult saved in: ', objectfile)

# Función para mostrar las personas detectadas en la imagen.
def show_people(image_filename, detected_people):
    print('\nAnnotation objects...')

    # Se abre la imagen.
    image = Image.open(image_filename)
    fig = plt.figure(figsize=(image.width/100, image.height/100))
    plt.axis('off')
    draw = ImageDraw.Draw(image)
    color = 'cyan'

    # Se dibujan los cuadros alrededor de las personas detectadas.
    for detected_person in detected_people:
        if detected_person.confidence > 0.2:
            r = detected_person.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)

    # Se muestra y guarda la imagen anotada.
    plt.imshow(image)
    plt.tight_layout(pad=0)
    objectfile = 'EPICA_OMEGA_person.jpg'
    fig.savefig(objectfile)
    print('\nResult saved in: ', objectfile)

# Punto de entrada del script.
if __name__ == '__main__':
    main()


"""
Ahora, desde la terminar, corre el comando:
python Analisis_de_Imagenes.py images/Galaxia.jpeg

El 'images/Galaxia.jpeg' es el parametro que indica la imagen que se va a analizar.
Es decir, se cambia segun la imagen que se requiera analizar.
"""