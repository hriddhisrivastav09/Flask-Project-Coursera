"""Local stand-in for the Watson EmotionPredict endpoint (offline verification only)."""

from flask import Flask, jsonify, request

app = Flask("mock_watson")
KEYWORDS = {
    "joy": ("glad", "happy", "love"),
    "anger": ("mad", "angry"),
    "disgust": ("disgust",),
    "sadness": ("sad",),
    "fear": ("afraid", "scared"),
}


@app.route("/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict", methods=["POST"])
def predict():
    """Mimic the Watson response format."""
    text = (request.get_json().get("raw_document", {}).get("text") or "").strip()
    if not text:
        return jsonify({"code": 3, "message": "empty text"}), 400
    scores = {k: 0.02 for k in ("anger", "disgust", "fear", "joy", "sadness")}
    for emotion, words in KEYWORDS.items():
        if any(w in text.lower() for w in words):
            scores[emotion] = 0.91
    return jsonify({"emotionPredictions": [{"emotion": scores, "target": ""}]})


if __name__ == "__main__":
    app.run(port=5001)
