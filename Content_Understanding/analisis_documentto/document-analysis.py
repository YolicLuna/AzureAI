from dotenv import load_dotenv
import os

# Se importan las librerias necesarias para autenticación y ánalisis de documentos.
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient


def main():

    # Se crea una función para limpiar la pantalla antes de mistrar los resultados.
    os.system('cls' if os.name=='nt' else 'clear')

    try:
        # Se cargan las variables de entorno para la autenticación.
        load_dotenv('env.txt') 
        endpoint = os.getenv('ENDPOINT')
        key = os.getenv('KEY')


        # Se define la url del documento que se va a analizar, el idioma y el modelo preconstruido que se usara.
        fileUri = "https://raw.githubusercontent.com/YolicLuna/AzureAI/6668cc8bebbf3b70c0e45d5df9c577c057edb12d/G139242591_6c06ee004815464fb0cfa6095f43c601.pdf"
        fileLocale = "en-US"
        fileModelId = "prebuilt-invoice"

        print(f"\nConnecting to Forms Recognizer at: {endpoint}")
        print(f"Analyzing invoice at: {fileUri}")


        # Se crea el cliente de análisis usando el endpoint y la clave de autenticación.

        document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))

        # Se llama a la funcicón de análisis usando la url del documento, el modelo preconstruido y el idioma.

        poller = document_analysis_client.begin_analyze_document_from_url(
            fileModelId, fileUri, locale=fileLocale)

        # Se espera a que el análisis se complete y se obtienen los resultados.
        receipts = poller.result()
        
        # Se crea un ciclo for para iterar sobre los resultados obtenidos y se imprimen los campos de interés.

        for idx, receipt in enumerate(receipts.documents):
            
            vendor_name = receipt.fields.get("VendorName")
            if vendor_name:
                print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

            customer_name = receipt.fields.get("CustomerName")
            if customer_name:
                print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")


            invoice_total = receipt.fields.get("InvoiceTotal")
            if invoice_total:
                print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")

    # Se maneja cualquier excepción que pueda ocurrir.
    except Exception as ex:
        print(ex)

    # Se imprime el mensaje de exito al finalizar el análisis.
    print("\nAnalysis complete.\n")

if __name__ == "__main__":
    main()        



"""
El primer resultado que arroja el análisis es:
Connecting to Forms Recognizer at: https://moondev.cognitiveservices.azure.com/
Analyzing invoice at: https://github.com/MicrosoftLearning/mslearn-ai-information-extraction/blob/main/Labfiles/prebuilt-doc-intelligence/sample-invoice/sample-invoice.pdf?raw=true

Vendor Name: CONTOSO LTD., with confidence 0.937.
Customer Name: 'MICROSOFT CORPORATION, with confidence 0.919.
Invoice Total: '$110.0, with confidence 0.969.

Analysis complete.

El segundo resultado que arroja el análisis es:
Connecting to Forms Recognizer at: https://moondev.cognitiveservices.azure.com/
Analyzing invoice at: https://raw.githubusercontent.com/YolicLuna/AzureAI/6668cc8bebbf3b70c0e45d5df9c577c057edb12d/G139242591_6c06ee004815464fb0cfa6095f43c601.pdf

Vendor Name: Microsoft, with confidence 0.83.
Customer Name: 'José, with confidence 0.685.
Invoice Total: 'USD0.59, with confidence 0.937.

Analysis complete.


Ambos resultados son correctos, ya que se logra la conección con el servicio, encuentra y análiza correctamente el documento y
por ultimo, extrae e imprime los campos que se le indicaron junto con su nivel de confianza.
"""


# Cabe señalar que al terminar las practicas, se eliminaron los recursos creados para evitar cargos innecesarios.
# Ademas de que la url del segundo documento ya no esta disponible, por lo que si quieres probar el codigo puedes hacerlo con la primer url.