"""
This file contains my flask implementation
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods = ["GET"])
def emotion_detector_function():
    """
    This method calls the emotion detector based on route call
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result["dominant_emotion"] is None:
        return "Invalid Input. Try Again Later!!"
    else:
        return (f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}.")

@app.route("/")
def index_page():
    """
    This method calls the index.html page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
