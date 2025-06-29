# Scroll Configuration Settings
# Modify these values to adjust scroll behavior

# Scroll speed settings
BASE_SCROLL_SPEED = 5          # Base scroll amount (higher = faster scrolling)
CONTINUOUS_SCROLL_MULTIPLIER = 2  # Multiplier for continuous scrolling speed

# Timing settings
SCROLL_COOLDOWN = 0.1          # Time between scroll actions (seconds)
SCROLL_GESTURE_HOLD_TIME = 0.3  # Time to hold gesture before continuous scrolling starts (seconds)

# Gesture detection settings
SCROLL_DISTANCE_THRESHOLD = 40  # Distance between fingers to trigger scroll (pixels)

# Visual feedback settings
SHOW_SCROLL_SPEED_INFO = True   # Show scroll speed information on screen
SHOW_GESTURE_STATUS = True      # Show current gesture status

# Advanced settings
ENABLE_CONTINUOUS_SCROLLING = True  # Enable/disable continuous scrolling
ENABLE_SCROLL_ERROR_HANDLING = True  # Enable error handling for scroll operations

# Scroll direction settings
SCROLL_UP_GESTURE = "index_pinky"    # Gesture for scroll up: "index_pinky" or "thumb_index"
SCROLL_DOWN_GESTURE = "thumb_index"  # Gesture for scroll down: "index_pinky" or "thumb_index"

# Performance settings
SCROLL_SMOOTHING_FACTOR = 0.8   # Smoothing factor for scroll gestures (0.0 to 1.0) 