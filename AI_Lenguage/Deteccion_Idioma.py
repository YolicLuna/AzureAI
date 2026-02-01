# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
import os

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

language_key = os.environ.get("LANGUAGE_KEY")
language_endpoint = os.environ.get("LANGUAGE_ENDPOINT")

if not language_key or not language_endpoint:
    raise ValueError("Missing LANGUAGE_KEY or LANGUAGE_ENDPOINT environment variables")

# Authenticate the client using your key and endpoint
def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint,
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Example method for detecting the language of text
def language_detection_example(client):
    try:
        documents = ["Hi, whats your name? Las palabras."]
        response = client.detect_language(documents = documents, country_hint = 'es')[0]
        print("Language: ", response.primary_language.name)

    except Exception as err:
        print("Encountered exception. {}".format(err))
language_detection_example(client)