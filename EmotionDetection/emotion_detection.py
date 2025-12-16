"""
This file uses Emotion Predict function of the Watson NLP Library to detect em
"""
import requests

def emotion_detector(text_to_analyze):
    """
    This function uses the text_to_analyze and pass it to the 
    Watson NLP Library to get the response
    """
    # Watson Emotion Predict Library URL
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    # Header params
    header_params = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Body params
    body_params = { "raw_document": { "text": text_to_analyze } }

    # API response
    response = requests.post(url, json = body_params, headers = header_params)

    return response.text
