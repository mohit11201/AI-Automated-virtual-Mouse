import autopy
import pyautogui
import time

class MouseController:
    def __init__(self):
        self.click_cooldown = 0.5  # seconds between clicks
        self.last_click_time = 0
        self.last_right_click_time = 0
        self.last_double_click_time = 0
        self.scroll_cooldown = 0.2
        self.last_scroll_time = 0
        self.last_drag_time = 0
        self.drag_cooldown = 0.1
        
        # Get screen dimensions
        self.wScr, self.hScr = autopy.screen.size()
        
    def left_click(self):
        """Perform left mouse click with cooldown"""
        current_time = time.time()
        if current_time - self.last_click_time > self.click_cooldown:
            autopy.mouse.click()
            self.last_click_time = current_time
            return True
        return False
    
    def right_click(self):
        """Perform right mouse click with cooldown"""
        current_time = time.time()
        if current_time - self.last_right_click_time > self.click_cooldown:
            autopy.mouse.click(button=autopy.mouse.Button.RIGHT)
            self.last_right_click_time = current_time
            return True
        return False
    
    def double_click(self):
        """Perform double mouse click with cooldown"""
        current_time = time.time()
        if current_time - self.last_double_click_time > self.click_cooldown:
            autopy.mouse.click()
            time.sleep(0.1)
            autopy.mouse.click()
            self.last_double_click_time = current_time
            return True
        return False
    
    def scroll_up(self, amount=3):
        """Scroll up with cooldown"""
        current_time = time.time()
        if current_time - self.last_scroll_time > self.scroll_cooldown:
            pyautogui.scroll(amount)
            self.last_scroll_time = current_time
            return True
        return False
    
    def scroll_down(self, amount=3):
        """Scroll down with cooldown"""
        current_time = time.time()
        if current_time - self.last_scroll_time > self.scroll_cooldown:
            pyautogui.scroll(-amount)
            self.last_scroll_time = current_time
            return True
        return False
    
    def move_mouse(self, x, y):
        """Move mouse to coordinates"""
        # Invert x coordinate for proper mapping
        autopy.mouse.move(self.wScr - x, y)
    
    def drag_mouse(self, x, y):
        """Drag mouse to coordinates (with mouse button held down)"""
        current_time = time.time()
        if current_time - self.last_drag_time > self.drag_cooldown:
            autopy.mouse.move(self.wScr - x, y)
            self.last_drag_time = current_time
            return True
        return False
    
    def get_screen_size(self):
        """Get screen dimensions"""
        return self.wScr, self.hScr
    
    def set_click_cooldown(self, cooldown):
        """Set click cooldown time"""
        self.click_cooldown = cooldown
    
    def set_scroll_cooldown(self, cooldown):
        """Set scroll cooldown time"""
        self.scroll_cooldown = cooldown

# Convenience functions for quick use
def left_click():
    """Quick left click function"""
    autopy.mouse.click()

def right_click():
    """Quick right click function"""
    autopy.mouse.click(button=autopy.mouse.Button.RIGHT)

def double_click():
    """Quick double click function"""
    autopy.mouse.click()
    time.sleep(0.1)
    autopy.mouse.click()

def scroll_up(amount=3):
    """Quick scroll up function"""
    pyautogui.scroll(amount)

def scroll_down(amount=3):
    """Quick scroll down function"""
    pyautogui.scroll(-amount)

def move_mouse(x, y):
    """Quick mouse move function"""
    wScr, hScr = autopy.screen.size()
    autopy.mouse.move(wScr - x, y)

# Example usage
if __name__ == "__main__":
    # Create a mouse controller instance
    mouse = MouseController()
    
    print("Mouse Functions Test")
    print("Available functions:")
    print("- mouse.left_click()")
    print("- mouse.right_click()")
    print("- mouse.double_click()")
    print("- mouse.scroll_up()")
    print("- mouse.scroll_down()")
    print("- mouse.move_mouse(x, y)")
    print("- mouse.drag_mouse(x, y)")
    
    # Test screen size
    w, h = mouse.get_screen_size()
    print(f"Screen size: {w}x{h}") 