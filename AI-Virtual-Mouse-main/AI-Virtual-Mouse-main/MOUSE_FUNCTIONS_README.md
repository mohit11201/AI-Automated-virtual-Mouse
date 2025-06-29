# AI Virtual Mouse - Enhanced Mouse Functions

This project provides enhanced mouse control functions for the AI Virtual Mouse system, including left-click, right-click, double-click, scrolling, and drag functionality.

## 📁 Files Overview

### Core Files
- **`enhanced_virtual_mouse.py`** - Enhanced version of the AI Virtual Mouse with additional gestures
- **`mouse_functions.py`** - Reusable mouse control module
- **`test_mouse_functions.py`** - Test script to verify mouse functions work correctly

### Original Files
- **`aivirtualmouseproject.py`** - Original AI Virtual Mouse implementation
- **`HandTrackingModule.py`** - Hand tracking and gesture detection module

## 🖱️ Available Mouse Functions

### 1. Basic Mouse Functions

#### Left Click
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.left_click()

# Using quick function
mouse_functions.left_click()
```

#### Right Click
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.right_click()

# Using quick function
mouse_functions.right_click()
```

#### Double Click
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.double_click()

# Using quick function
mouse_functions.double_click()
```

### 2. Mouse Movement

#### Move Mouse
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.move_mouse(x, y)

# Using quick function
mouse_functions.move_mouse(x, y)
```

#### Drag Mouse
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.drag_mouse(x, y)
```

### 3. Scrolling Functions

#### Scroll Up
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.scroll_up(amount=3)  # amount is optional

# Using quick function
mouse_functions.scroll_up(amount=3)
```

#### Scroll Down
```python
# Using the MouseController class
mouse = mouse_functions.MouseController()
mouse.scroll_down(amount=3)  # amount is optional

# Using quick function
mouse_functions.scroll_down(amount=3)
```

### 4. Utility Functions

#### Get Screen Size
```python
mouse = mouse_functions.MouseController()
width, height = mouse.get_screen_size()
print(f"Screen: {width}x{height}")
```

#### Set Cooldown Times
```python
mouse = mouse_functions.MouseController()
mouse.set_click_cooldown(0.3)    # Set click cooldown to 0.3 seconds
mouse.set_scroll_cooldown(0.1)   # Set scroll cooldown to 0.1 seconds
```

## 🎯 Enhanced Virtual Mouse Gestures

The enhanced virtual mouse supports the following hand gestures:

### Gesture Controls

| Gesture | Action | Description |
|---------|--------|-------------|
| **Index finger only** | Move Mouse | Move cursor around the screen |
| **Index + Middle** | Left Click | Perform left mouse click |
| **Index + Ring** | Right Click | Perform right mouse click |
| **Index + Middle + Ring** | Double Click | Perform double mouse click |
| **Index + Pinky** | Scroll Up | Scroll up in active window |
| **Thumb + Index** | Scroll Down | Scroll down in active window |
| **All fingers closed** | Drag Mode | Move mouse in drag mode |
| **Index + Pinky (legacy)** | Open A Drive | Open A: drive (if available) |

### Visual Feedback

The enhanced version provides real-time visual feedback:
- **Gesture name** displayed on screen
- **Color-coded circles** for different actions
- **FPS counter** for performance monitoring
- **Distance indicators** for click preparation

## 🚀 How to Use

### 1. Run the Enhanced Virtual Mouse
```bash
python enhanced_virtual_mouse.py
```

### 2. Test Mouse Functions
```bash
python test_mouse_functions.py
```

### 3. Use Mouse Functions in Your Code
```python
import mouse_functions

# Create a mouse controller
mouse = mouse_functions.MouseController()

# Perform actions
mouse.move_mouse(500, 300)
mouse.left_click()
mouse.right_click()
mouse.scroll_up()
```

## ⚙️ Configuration

### Cooldown Settings
- **Click cooldown**: 0.5 seconds (prevents accidental multiple clicks)
- **Scroll cooldown**: 0.2 seconds (prevents rapid scrolling)
- **Drag cooldown**: 0.1 seconds (smooth dragging)

### Screen Mapping
- **Frame reduction**: 100 pixels from edges
- **Smoothing**: 7 (for smooth mouse movement)
- **Coordinate inversion**: X-axis is inverted for proper mapping

## 🔧 Troubleshooting

### Common Issues

1. **MediaPipe DLL Error**
   ```bash
   # Solution: Reinstall MediaPipe
   pip uninstall mediapipe -y
   pip install mediapipe==0.10.5
   ```

2. **Missing Visual C++ Redistributable**
   - Download and install from: https://aka.ms/vs/17/release/vc_redist.x64.exe

3. **Camera not detected**
   - Check camera permissions
   - Try different camera index (0, 1, 2)

4. **Mouse movement too sensitive**
   - Adjust `smoothening` value in the code
   - Increase for smoother movement

### Performance Tips

1. **Reduce frame rate** for better performance
2. **Close unnecessary applications** to free up resources
3. **Ensure good lighting** for hand detection
4. **Keep hand within camera frame** for best tracking

## 📋 Requirements

```txt
opencv-python>=4.5.0
mediapipe>=0.8.0
autopy>=1.0.0
numpy>=1.19.0
pyautogui>=0.9.50
```

## 🎮 Advanced Usage

### Custom Gesture Recognition
```python
import mouse_functions
import HandTrackingModule as htm

detector = htm.handDetector()
mouse = mouse_functions.MouseController()

# Custom gesture detection
fingers = detector.fingersUp()
if fingers[1] == 1 and fingers[2] == 1:  # Index + Middle
    mouse.left_click()
```

### Integration with Other Projects
```python
from mouse_functions import MouseController

class MyApplication:
    def __init__(self):
        self.mouse = MouseController()
    
    def handle_gesture(self, gesture_type):
        if gesture_type == "left_click":
            self.mouse.left_click()
        elif gesture_type == "right_click":
            self.mouse.right_click()
```

## 📝 License

This project is part of the AI Virtual Mouse system. All mouse functions are designed to work with hand gesture recognition for accessible computing.

## 🤝 Contributing

Feel free to contribute by:
1. Adding new mouse functions
2. Improving gesture recognition
3. Optimizing performance
4. Adding new features

---

**Note**: Make sure to test mouse functions in a safe environment before using them in production applications. 