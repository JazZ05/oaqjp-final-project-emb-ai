"""
This file uses Emotion Predict function of the Watson NLP Library to detect em
"""
import requests
import json

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

    # Format the response to JSON
    formatted_response = json.loads(response.text)

    # check for successful response
    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        
        # Create list of score
        emotion_score_list = [anger_score, disgust_score, fear_score, joy_score, sadness_score]

        # Finding dominating emotion
        dominant_emotion_index_value = emotion_score_list.index(max(emotion_score_list)) # Finding the max value and getting the index of the value
        emotions_label_list = ["anger", "disgust", "fear", "joy", "sadness"] # Creating emotion label list
        dominant_emotion_label = emotions_label_list[dominant_emotion_index_value] # Getting label based on index
    else:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_label = None
    
    final_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_label
    }

    return final_response
