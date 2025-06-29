import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy
import os
import pyautogui
from scroll_config import *

#############################
wCam, hCam = 640, 480
frameR = 100  # frame Reduction
smoothening = 7
##############################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# Mouse control variables
click_cooldown = 0.5  # seconds between clicks
last_click_time = 0
last_right_click_time = 0
last_double_click_time = 0
last_scroll_time = 0

# Enhanced scroll variables (now using config)
scroll_speed = BASE_SCROLL_SPEED
continuous_scroll = ENABLE_CONTINUOUS_SCROLLING
scroll_gesture_hold_time = SCROLL_GESTURE_HOLD_TIME
last_scroll_gesture_time = 0
scroll_gesture_active = False

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()

def perform_click(click_type="left"):
    """Perform mouse click with cooldown"""
    global last_click_time, last_right_click_time, last_double_click_time
    current_time = time.time()
    
    if click_type == "left":
        if current_time - last_click_time > click_cooldown:
            autopy.mouse.click()
            last_click_time = current_time
            return True
    elif click_type == "right":
        if current_time - last_right_click_time > click_cooldown:
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
            last_right_click_time = current_time
            return True
    elif click_type == "double":
        if current_time - last_double_click_time > click_cooldown:
            autopy.mouse.click()
            time.sleep(0.1)
            autopy.mouse.click()
            last_double_click_time = current_time
            return True
    return False

def perform_scroll(direction="up", continuous=False):
    """Enhanced scroll function with variable speed and continuous scrolling"""
    global last_scroll_time, scroll_gesture_active, last_scroll_gesture_time
    current_time = time.time()
    
    # Calculate scroll amount based on direction and continuous mode
    if continuous:
        scroll_amount = scroll_speed * CONTINUOUS_SCROLL_MULTIPLIER
    else:
        scroll_amount = scroll_speed
    
    if direction == "down":
        scroll_amount = -scroll_amount
    
    # Check if we should scroll
    should_scroll = False
    
    if continuous:
        # For continuous scrolling, check if gesture is held
        if current_time - last_scroll_gesture_time > scroll_gesture_hold_time:
            if current_time - last_scroll_time > SCROLL_COOLDOWN:
                should_scroll = True
                last_scroll_time = current_time
    else:
        # For single scroll, use normal cooldown
        if current_time - last_scroll_time > SCROLL_COOLDOWN:
            should_scroll = True
            last_scroll_time = current_time
    
    if should_scroll:
        try:
            pyautogui.scroll(int(scroll_amount))
            return True
        except Exception as e:
            if ENABLE_SCROLL_ERROR_HANDLING:
                print(f"Scroll error: {e}")
            return False
    
    return False

def is_thumb_up(lmList):
    """Enhanced thumb detection that works for both left and right hands"""
    if len(lmList) < 21:
        return False
    
    # Get thumb landmarks
    thumb_tip = lmList[4]  # Thumb tip
    thumb_ip = lmList[3]   # Thumb IP joint
    thumb_mcp = lmList[2]  # Thumb MCP joint
    
    # For left hand (thumb on left side)
    if thumb_tip[1] < thumb_ip[1]:
        return True
    # For right hand (thumb on right side)  
    elif thumb_tip[1] > thumb_ip[1]:
        return True
    
    return False

def draw_gesture_info(img, gesture_name, color=(0, 255, 0)):
    """Draw gesture information on the image"""
    if SHOW_GESTURE_STATUS:
        cv2.putText(img, f"Gesture: {gesture_name}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

def draw_scroll_info(img, direction, speed):
    """Draw scroll information on the image"""
    if SHOW_SCROLL_SPEED_INFO:
        cv2.putText(img, f"Scroll {direction} (Speed: {speed})", (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

print("AI Virtual Mouse - Enhanced Version with Improved Scrolling")
print("Controls:")
print("- Index finger only: Move mouse")
print("- Index + Middle finger: Left click")
print("- Index + Ring finger: Right click")
print("- Index + Middle + Ring: Double click")
print("- Index + Pinky: Scroll up (hold for continuous)")
print("- Thumb + Index: Scroll down (hold for continuous)")
print("- All fingers closed: Drag mode")
print("Press 'ESC' to exit")
print(f"\nScroll Settings:")
print(f"- Base Speed: {BASE_SCROLL_SPEED}")
print(f"- Continuous Multiplier: {CONTINUOUS_SCROLL_MULTIPLIER}")
print(f"- Cooldown: {SCROLL_COOLDOWN}s")
print(f"- Hold Time: {SCROLL_GESTURE_HOLD_TIME}s")

while True:
    # 1. Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger
        x2, y2 = lmList[12][1:]  # Middle finger
        x3, y3 = lmList[16][1:]  # Ring finger
        x4, y4 = lmList[20][1:]  # Pinky finger
        x5, y5 = lmList[4][1:]   # Thumb

        # 3. Check which fingers are up
        fingers = detector.fingersUp()
        
        # Enhanced thumb detection
        thumb_up = is_thumb_up(lmList)
        
        cv2.rectangle(img, (frameR, frameR), (wCam-frameR, hCam-frameR), (255, 0, 255), 2)

        # 4. Only index finger: Moving mode
        if fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and not thumb_up:
            # Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse
            autopy.mouse.move(wScr-clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            draw_gesture_info(img, "Move Mouse", (255, 0, 255))

        # 5. Index and middle finger: Left Clicking mode
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0 and not thumb_up:
            # Find distance between fingers 
            length, img, lineInfo = detector.findDistance(8, 12, img)
            
            # Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                if perform_click("left"):
                    draw_gesture_info(img, "Left Click", (0, 255, 0))
            else:
                draw_gesture_info(img, "Prepare Left Click", (255, 255, 0))

        # 6. Index and ring finger: Right Clicking mode
        elif fingers[1] == 1 and fingers[3] == 1 and fingers[2] == 0 and fingers[4] == 0 and not thumb_up:
            # Find distance between fingers 
            length, img, lineInfo = detector.findDistance(8, 16, img)
            
            # Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 0, 255), cv2.FILLED)
                if perform_click("right"):
                    draw_gesture_info(img, "Right Click", (0, 0, 255))
            else:
                draw_gesture_info(img, "Prepare Right Click", (255, 255, 0))

        # 7. Index, middle, and ring finger: Double Click mode
        elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0 and not thumb_up:
            # Find distance between index and middle fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            
            # Double click if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 0, 0), cv2.FILLED)
                if perform_click("double"):
                    draw_gesture_info(img, "Double Click", (255, 0, 0))
            else:
                draw_gesture_info(img, "Prepare Double Click", (255, 255, 0))

        # 8. Index and pinky finger: Scroll Up mode (enhanced)
        elif fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0 and fingers[3] == 0 and not thumb_up:
            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 20, img)
            
            # Scroll if distance short
            if length < SCROLL_DISTANCE_THRESHOLD:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (255, 255, 0), cv2.FILLED)
                
                # Update gesture time for continuous scrolling
                if not scroll_gesture_active:
                    last_scroll_gesture_time = time.time()
                    scroll_gesture_active = True
                
                # Perform scroll (continuous if held)
                if perform_scroll("up", continuous=True):
                    draw_gesture_info(img, "Scroll Up", (255, 255, 0))
                    draw_scroll_info(img, "UP", scroll_speed * CONTINUOUS_SCROLL_MULTIPLIER)
                else:
                    draw_gesture_info(img, "Scroll Up (Holding)", (255, 255, 0))
            else:
                scroll_gesture_active = False
                draw_gesture_info(img, "Prepare Scroll Up", (255, 255, 0))

        # 9. Thumb and index finger: Scroll Down mode (enhanced)
        elif thumb_up and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            # Find distance between thumb and index
            length, img, lineInfo = detector.findDistance(4, 8, img)
            
            # Scroll if distance short
            if length < SCROLL_DISTANCE_THRESHOLD:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                
                # Update gesture time for continuous scrolling
                if not scroll_gesture_active:
                    last_scroll_gesture_time = time.time()
                    scroll_gesture_active = True
                
                # Perform scroll (continuous if held)
                if perform_scroll("down", continuous=True):
                    draw_gesture_info(img, "Scroll Down", (0, 255, 255))
                    draw_scroll_info(img, "DOWN", scroll_speed * CONTINUOUS_SCROLL_MULTIPLIER)
                else:
                    draw_gesture_info(img, "Scroll Down (Holding)", (0, 255, 255))
            else:
                scroll_gesture_active = False
                draw_gesture_info(img, "Prepare Scroll Down", (255, 255, 0))

        # 10. All fingers closed: Drag mode
        elif fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            # Convert Coordinates for drag
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScr))

            # Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse with drag
            autopy.mouse.move(wScr-clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (128, 0, 128), cv2.FILLED)
            plocX, plocY = clocX, clocY
            draw_gesture_info(img, "Drag Mode", (128, 0, 128))

        # 11. Index and middle finger + ring finger: Open A Drive mode (legacy)
        elif fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0 and fingers[3] == 0 and not thumb_up:
            # Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 20, img)

            # Open A Drive if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                try:
                    os.startfile("A:\\")
                    draw_gesture_info(img, "Opening A Drive", (0, 255, 0))
                except:
                    draw_gesture_info(img, "A Drive not found", (0, 0, 255))
        else:
            # Reset scroll gesture state when no scroll gesture is active
            scroll_gesture_active = False

    # Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (10, 90), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
   
    # Display
    cv2.imshow("AI Virtual Mouse - Enhanced", img)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows() 