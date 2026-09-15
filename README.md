# Tensor Lens
## [🆕 Video - Tensor Lens](https://youtu.be/z4JPktiZjqI)
## [Video - Tensor Lens](https://youtu.be/HZD79x6fGqw)

A small Flask app that loads an image as an RGB NumPy tensor and renders it on an HTML canvas.

## Features

- Loads an RGB image into a NumPy tensor and renders it on an HTML canvas.
- Adjusts red, green, and blue channels with live sliders.
- Uploads a replacement image and downloads the adjusted canvas as a PNG.
- Adds polygon points by clicking on the canvas.
- Connects the points into a closed, highlighted selection with **Create selection area**.
- Applies channel adjustments only inside the selection while it is active.
- Applies channel adjustments to the entire canvas when no selection is active.
- Removes all points, lines, and selection highlighting with **Clear selected area**.
- Commits the current slider changes to the tensor with **Update tensor**, clears the selection, and keeps the updated image for future selections.
- Keeps every committed image tensor in a stack. **Undo last tensor** removes the newest committed tensor and restores the previous canvas.
- Starts each upload with an original-image tensor and a first stack entry. **Select original pixels** restores the selected polygon from that original tensor when the next update is committed; **Select latest tensor** uses the latest stack entry.
- Downloads the latest tensor shown on the canvas.

## Run

Install Python 3.10+ first, then from this folder run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000.

Put an image named `sample.png` beside `app.py` to use your own image. If it is missing, the Python script creates a small RGB gradient image automatically.

The `/api/tensor` endpoint returns the tensor as JSON with shape `height x width x 3`; the canvas applies the three channel offsets live and clamps every displayed value to `0-255`.
