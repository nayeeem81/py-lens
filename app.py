from pathlib import Path

from flask import Flask, jsonify, render_template

from tensor_image import load_rgb_tensor, tensor_payload


app = Flask(__name__)
IMAGE_PATH = Path(__file__).with_name("sample.png")


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/tensor")
def tensor():
    return jsonify(tensor_payload(load_rgb_tensor(IMAGE_PATH)))


if __name__ == "__main__":
    app.run(debug=True)
