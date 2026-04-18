import os
import pickle
import uuid
import base64
import numpy as np
from io import BytesIO
from PIL import Image

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from tensorflow.keras.models import load_model


# ------------------------------------------------------------
# Load model once at startup
# ------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = load_model(os.path.join(BASE_DIR, "burn_model_final.keras"))

with open(os.path.join(BASE_DIR, "labels.pkl"), "rb") as f:
    class_labels = pickle.load(f)


# ------------------------------------------------------------
# HOME PAGE
# ------------------------------------------------------------
def home(request):
    return render(request, "home.html")


# ------------------------------------------------------------
# PREDICTION PAGE + RESULT
# ------------------------------------------------------------
def predict(request):

    if request.method == "POST":

        img = None
        uploaded_file_url = None

        # ─────────────────────────────────────────────────────
        # CASE 1 — File upload from upload page
        # ─────────────────────────────────────────────────────
        if request.FILES.get("image"):

            img_file = request.FILES["image"]

            fs = FileSystemStorage()
            filename = fs.save(img_file.name, img_file)
            uploaded_file_url = fs.url(filename)

            # Re-open from saved file so PIL can read it cleanly
            img = Image.open(fs.path(filename)).convert("RGB")

        # ─────────────────────────────────────────────────────
        # CASE 2 — Base64 image from live camera
        # ─────────────────────────────────────────────────────
        elif request.POST.get("captured_image"):

            data_url = request.POST.get("captured_image")

            # Split "data:image/jpeg;base64,/9j/4AAQ..."
            try:
                header, imgstr = data_url.split(";base64,")
                ext = header.split("/")[-1]   # jpeg or png
                if ext not in ["jpeg", "jpg", "png", "webp"]:
                    ext = "jpeg"
            except Exception:
                return redirect("home")

            # Decode base64 → bytes → PIL image
            img_data = base64.b64decode(imgstr)
            img = Image.open(BytesIO(img_data)).convert("RGB")

            # Save decoded image so result page can display it
            filename = f"camera_{uuid.uuid4().hex}.{ext}"
            fs = FileSystemStorage()
            saved_name = fs.save(filename, BytesIO(img_data))
            uploaded_file_url = fs.url(saved_name)

        # ─────────────────────────────────────────────────────
        # Neither — redirect back to home
        # ─────────────────────────────────────────────────────
        else:
            return redirect("home")

        # ─────────────────────────────────────────────────────
        # Preprocess → predict
        # ─────────────────────────────────────────────────────
        img_resized = img.resize((224, 224))
        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred_probs = model.predict(img_array)
        pred_class = np.argmax(pred_probs)

        label      = class_labels[pred_class]
        confidence = int(np.max(pred_probs) * 100)

        context = {
            "label":      label,
            "confidence": confidence,
            "image_url":  uploaded_file_url,
        }

        return render(request, "result.html", context)

    # GET request — redirect to home
    return redirect("home")


# ------------------------------------------------------------
# OTHER PAGES
# ------------------------------------------------------------
def guide(request):
    return render(request, "guide.html")

def emergency(request):
    return render(request, "emergency.html")

def about(request):
    return render(request, "about.html")

def upload_page(request):
    return render(request, "upload.html")

def live_page(request):
    return render(request, "live.html")