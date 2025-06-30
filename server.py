"""Flask web server for the Emotion Detector application."""
from flask import Flask, request, jsonify, render_template
from Emotion_detector.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """API endpoint for emotion detection. Returns formatted emotion analysis or error message."""
    data = request.get_json()
    text = data.get('text', '')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return jsonify({'response': 'Invalid text! Please try again!'})
    response_str = (f"For the given statement, the system response is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}. "
                   f"The dominant emotion is {result['dominant_emotion']}.")
    return jsonify({'response': response_str})

if __name__ == '__main__':
    # Run the Flask development server on localhost:5000
    app.run(host='localhost', port=5000, debug=True) 