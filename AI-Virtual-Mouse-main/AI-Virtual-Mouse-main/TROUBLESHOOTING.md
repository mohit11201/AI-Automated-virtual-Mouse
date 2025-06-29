# AI Virtual Mouse - Troubleshooting Guide

## Main Issue: Python Version Compatibility

**Problem**: You're using Python 3.13.3, but Mediapipe doesn't support Python 3.13 yet.

**Solutions**:

### Option 1: Downgrade Python (Recommended)
1. Install Python 3.11 or 3.12 from [python.org](https://www.python.org/downloads/)
2. Create a virtual environment with the older Python version:
   ```bash
   python3.11 -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Option 2: Use Conda (Alternative)
1. Install Anaconda or Miniconda
2. Create environment with Python 3.11:
   ```bash
   conda create -n virtualmouse python=3.11
   conda activate virtualmouse
   pip install -r requirements.txt
   ```

### Option 3: Use Docker
1. Create a Dockerfile:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "aivirtualmouseproject.py"]
   ```

## Other Common Issues

### 1. Camera Access
- Make sure your webcam is connected and working
- Check if other applications can access your camera
- Try changing camera index: `cv2.VideoCapture(1)` instead of `cv2.VideoCapture(0)`

### 2. Permission Issues (Windows)
- Run as Administrator if you get permission errors
- Make sure antivirus isn't blocking the application

### 3. Dependencies Installation
If you get errors installing dependencies:
```bash
pip install --upgrade pip
pip install opencv-python
pip install mediapipe
pip install autopy
pip install numpy
pip install pyautogui
```

### 4. Hand Detection Issues
- Ensure good lighting
- Keep your hand clearly visible to the camera
- Make sure your hand is within the frame boundaries

## How to Use the Fixed Application

1. **Mouse Movement**: Raise only your index finger
2. **Left Click**: Raise index and middle fingers, then bring them close together
3. **Right Click**: Raise index and ring fingers, then bring them close together
4. **Open A Drive**: Raise index and pinky fingers, then bring them close together
5. **Exit**: Press ESC key

## Testing the Installation

After installing dependencies, test with:
```bash
python -c "import cv2, mediapipe, autopy, numpy; print('All dependencies working!')"
```

If successful, run the main application:
```bash
python aivirtualmouseproject.py
``` 