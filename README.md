# Emotion Detector

An AI-based web application that detects emotions (anger, disgust, fear, joy, sadness)
and the dominant emotion in a statement, using the Watson NLP `EmotionPredict` service,
packaged as the `EmotionDetection` Python package and served with Flask.

## Project layout

| Path | Purpose |
|------|---------|
| `EmotionDetection/emotion_detection.py` | `emotion_detector()` calls Watson NLP, formats output, handles status 400 |
| `EmotionDetection/__init__.py` | Makes `EmotionDetection` a package |
| `server.py` | Flask app (`/` and `/emotionDetector`) with blank-input handling |
| `test_emotion_detection.py` | Unit tests (joy, anger, disgust, sadness, fear) |
| `templates/`, `static/` | Web UI |
| `screenshots/` | `6b_deployment_test.png`, `7c_error_handling_interface.png` |

## Run

```bash
pip install -r requirements.txt
python3 server.py                      # http://localhost:5000
python3 -m unittest -v test_emotion_detection
pylint server.py
```

The Watson URL can be overridden with the `WATSON_URL` environment variable.
