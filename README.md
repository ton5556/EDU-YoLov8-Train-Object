# EDU-YoLov8-Train-Object

A small educational project for training a **YOLOv8** object detection model — set up here to detect **cars and motorcycles**, using a dataset labeled with [Roboflow](https://roboflow.com/).

##  Project Structure

```
EDU-YoLov8-Train-Object/
├── datasets/           # Training/validation data (YOLO format)
├── img/                # Sample images for inference/testing
├── runs/detect/        # Output from detection/training runs
├── train.py            # Train the YOLOv8 model
├── detect.py            # Run detection/inference with a trained model
├── test_model.py        # Test / evaluate a trained model
├── export_onnx.py       # Export the trained model to ONNX format
├── fitter_img.py         # Image preprocessing utility
├── vdo_cut.py            # Cut/extract frames or clips from video
├── vdo.txt               # Notes / list related to video processing
├── How to train ai for detection Car and motorcycle by Roboflow.docx
│                        # Step-by-step guide for building the dataset in Roboflow
└── README.md
```

##  Setup

**Requirements:** Python 3.9+ and a CUDA-capable GPU (recommended) for faster training.

1. Clone the repository and move into it:
   ```bash
   git clone https://github.com/ton5556/EDU-YoLov8-Train-Object.git
   cd EDU-YoLov8-Train-Object
   ```

2. Create and activate a virtual environment (Windows):
   ```bash
   python -m venv venv
   venv\Scripts\activate.bat
   ```

   On macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
   pip install ultralytics
   ```

4. Open the project in your editor (optional):
   ```bash
   code .
   ```

##  Usage

### Train the model
```bash
python train.py
```

### Run detection on an image or video
```bash
python detect.py
```

### Test / evaluate the trained model
```bash
python test_model.py
```

### Export to ONNX
```bash
python export_onnx.py
```

### Extract frames/clips from a video for dataset building
```bash
python vdo_cut.py
```

##  Dataset

The dataset was labeled using **Roboflow**. See `How to train ai for detection Car and motorcycle by Roboflow.docx` for a full walkthrough of the labeling and export process, and place your exported dataset inside the `datasets/` folder before running `train.py`.
