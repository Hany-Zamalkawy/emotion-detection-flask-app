"""
Executing this file initiates the application of emotion
detection over a Flask channel.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask application
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Retrieves text from request arguments, passes it to the detector model,
    and returns a formatted string containing the system response.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Handle blank response evaluation (Task 7 requirement)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Standard presentation string format
    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Renders the main index page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
