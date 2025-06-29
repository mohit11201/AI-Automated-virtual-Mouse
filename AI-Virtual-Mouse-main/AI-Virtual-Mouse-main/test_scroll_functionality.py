#!/usr/bin/env python3
"""
Test Script for Enhanced Scroll Functionality
This script helps verify that the scrolling features are working properly.
"""

import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
from scroll_config import *

def test_scroll_detection():
    """Test scroll gesture detection without actually scrolling"""
    print("Testing Scroll Gesture Detection...")
    print("This test will show you when scroll gestures are detected.")
    print("Press 'ESC' to exit the test.")
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    detector = htm.handDetector(maxHands=1)
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        
        if len(lmList) != 0:
            fingers = detector.fingersUp()
            
            # Test thumb detection
            thumb_up = False
            if len(lmList) >= 21:
                thumb_tip = lmList[4]
                thumb_ip = lmList[3]
                if thumb_tip[1] < thumb_ip[1] or thumb_tip[1] > thumb_ip[1]:
                    thumb_up = True
            
            # Test scroll up gesture (index + pinky)
            if fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0 and fingers[3] == 0 and not thumb_up:
                length, img, lineInfo = detector.findDistance(8, 20, img)
                if length < SCROLL_DISTANCE_THRESHOLD:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "SCROLL UP DETECTED", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "PREPARE SCROLL UP", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            
            # Test scroll down gesture (thumb + index)
            elif thumb_up and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                length, img, lineInfo = detector.findDistance(4, 8, img)
                if length < SCROLL_DISTANCE_THRESHOLD:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                    cv2.putText(img, "SCROLL DOWN DETECTED", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                else:
                    cv2.putText(img, "PREPARE SCROLL DOWN", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            
            # Show finger status
            cv2.putText(img, f"Thumb: {thumb_up}", (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(img, f"Fingers: {fingers}", (10, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Scroll Gesture Test", img)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def test_actual_scrolling():
    """Test actual scrolling functionality"""
    print("Testing Actual Scrolling...")
    print("This test will perform actual scroll actions.")
    print("Make sure you have a scrollable window open (like a web browser).")
    print("Press 'ESC' to exit the test.")
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    detector = htm.handDetector(maxHands=1)
    last_scroll_time = 0
    
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        
        if len(lmList) != 0:
            fingers = detector.fingersUp()
            
            # Test thumb detection
            thumb_up = False
            if len(lmList) >= 21:
                thumb_tip = lmList[4]
                thumb_ip = lmList[3]
                if thumb_tip[1] < thumb_ip[1] or thumb_tip[1] > thumb_ip[1]:
                    thumb_up = True
            
            current_time = time.time()
            
            # Test scroll up gesture
            if fingers[1] == 1 and fingers[4] == 1 and fingers[2] == 0 and fingers[3] == 0 and not thumb_up:
                length, img, lineInfo = detector.findDistance(8, 20, img)
                if length < SCROLL_DISTANCE_THRESHOLD:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, "SCROLLING UP", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    if current_time - last_scroll_time > SCROLL_COOLDOWN:
                        try:
                            pyautogui.scroll(BASE_SCROLL_SPEED)
                            last_scroll_time = current_time
                            print("Scroll UP performed")
                        except Exception as e:
                            print(f"Scroll error: {e}")
            
            # Test scroll down gesture
            elif thumb_up and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                length, img, lineInfo = detector.findDistance(4, 8, img)
                if length < SCROLL_DISTANCE_THRESHOLD:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 255), cv2.FILLED)
                    cv2.putText(img, "SCROLLING DOWN", (10, 30), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                    
                    if current_time - last_scroll_time > SCROLL_COOLDOWN:
                        try:
                            pyautogui.scroll(-BASE_SCROLL_SPEED)
                            last_scroll_time = current_time
                            print("Scroll DOWN performed")
                        except Exception as e:
                            print(f"Scroll error: {e}")
        
        cv2.imshow("Actual Scroll Test", img)
        if cv2.waitKey(1) == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Enhanced Scroll Functionality Test")
    print("=" * 40)
    print("1. Test scroll gesture detection (no actual scrolling)")
    print("2. Test actual scrolling functionality")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            test_scroll_detection()
        elif choice == "2":
            test_actual_scrolling()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 