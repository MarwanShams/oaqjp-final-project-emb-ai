
"""Emotion detection using IBM Watson NLP."""

import json
import requests


def emotion_detector(text_to_analyze):
    """Analyze text and return emotion scores and dominant emotion."""

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers,
        timeout=30
    )

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    emotion_scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"]
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores
