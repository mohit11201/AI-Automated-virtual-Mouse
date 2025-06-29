#!/usr/bin/env python3
"""
Test script for mouse functions
This script demonstrates how to use the mouse functions module
"""

import time
import mouse_functions

def test_mouse_functions():
    """Test various mouse functions"""
    print("Testing Mouse Functions...")
    print("=" * 40)
    
    # Create mouse controller instance
    mouse = mouse_functions.MouseController()
    
    # Get screen size
    w, h = mouse.get_screen_size()
    print(f"Screen size: {w}x{h}")
    
    # Test 1: Move mouse to center of screen
    print("\n1. Moving mouse to center of screen...")
    center_x, center_y = w // 2, h // 2
    mouse.move_mouse(center_x, center_y)
    time.sleep(1)
    
    # Test 2: Left click
    print("2. Performing left click...")
    mouse.left_click()
    time.sleep(1)
    
    # Test 3: Right click
    print("3. Performing right click...")
    mouse.right_click()
    time.sleep(1)
    
    # Test 4: Double click
    print("4. Performing double click...")
    mouse.double_click()
    time.sleep(1)
    
    # Test 5: Scroll up
    print("5. Scrolling up...")
    mouse.scroll_up()
    time.sleep(1)
    
    # Test 6: Scroll down
    print("6. Scrolling down...")
    mouse.scroll_down()
    time.sleep(1)
    
    # Test 7: Move mouse to different positions
    print("7. Moving mouse to different positions...")
    positions = [
        (w // 4, h // 4),      # Top-left quadrant
        (3 * w // 4, h // 4),  # Top-right quadrant
        (3 * w // 4, 3 * h // 4),  # Bottom-right quadrant
        (w // 4, 3 * h // 4),  # Bottom-left quadrant
    ]
    
    for i, (x, y) in enumerate(positions, 1):
        print(f"   Moving to position {i}: ({x}, {y})")
        mouse.move_mouse(x, y)
        time.sleep(0.5)
    
    print("\nAll tests completed!")
    print("=" * 40)

def test_quick_functions():
    """Test quick convenience functions"""
    print("\nTesting Quick Functions...")
    print("=" * 40)
    
    # Get screen size
    w, h = mouse_functions.autopy.screen.size()
    print(f"Screen size: {w}x{h}")
    
    # Test quick functions
    print("\n1. Quick left click...")
    mouse_functions.left_click()
    time.sleep(1)
    
    print("2. Quick right click...")
    mouse_functions.right_click()
    time.sleep(1)
    
    print("3. Quick double click...")
    mouse_functions.double_click()
    time.sleep(1)
    
    print("4. Quick scroll up...")
    mouse_functions.scroll_up()
    time.sleep(1)
    
    print("5. Quick scroll down...")
    mouse_functions.scroll_down()
    time.sleep(1)
    
    print("6. Quick mouse move...")
    mouse_functions.move_mouse(w // 2, h // 2)
    
    print("\nQuick functions test completed!")
    print("=" * 40)

if __name__ == "__main__":
    print("Mouse Functions Test Script")
    print("This script will test various mouse functions.")
    print("Make sure you have a window focused where you want to test clicks.")
    print("Press Enter to start testing...")
    input()
    
    try:
        test_mouse_functions()
        test_quick_functions()
        print("\nAll tests passed successfully!")
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("Make sure all required packages are installed.")
    
    print("\nPress Enter to exit...")
    input() 