import os
import datetime

class Screenshot:
    @staticmethod
    def capture_screenshot(driver):
        print("capturing screenshotpath")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = "/Users/tamil/Desktop/PythonSeleniumDemo/Projects/screenshot"

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_filename = f"screenshot_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
        absolute_screenshot_path = os.path.abspath(screenshot_path)
        if os.path.isdir(screenshot_dir) and os.access(screenshot_dir, os.W_OK):
            driver.save_screenshot(absolute_screenshot_path)        
        return absolute_screenshot_path
