import subprocess
import time
import json
from playwright.sync_api import sync_playwright

# def load_credentials(file_path='credentials.json'):
#     try:
#         with open(file_path, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         print(f"Credentials file {file_path} not found")
#         return None
#     except json.JSONDecodeError:
#         print("Invalid JSON in credentials file")
#         return None

def connect_wifi(ssid):
    try:
        subprocess.run(['netsh', 'wlan', 'disconnect'], capture_output=True)
        time.sleep(2)
        
        connect_cmd = ['netsh', 'wlan', 'connect', f'name={ssid}']
        result = subprocess.run(connect_cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Connected to {ssid}")
            return True
        else:
            print(f"WiFi connection failed: {result.stderr}")
            return False
    
    except Exception as e:
        print(f"WiFi connection error: {e}")
        return False

def login_sonicwall(url, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        
        try:
            page.goto(url)
            
            username_selector = "div.sw-login__input-cont > div:nth-of-type(1) input"
            page.fill(username_selector, username)
            
            password_selector = "div.sw-login__input-cont > div:nth-of-type(2) input"
            page.fill(password_selector, password)
            
            login_button_selector = "div.sw-login__trigger-cont > div"
            page.click(login_button_selector)
            
            continue_button_selector = "button:has-text('Continue')"
            page.click(continue_button_selector)
            
            print("Login successful!")
        
        except Exception as e:
            print(f"Login failed: {e}")
        
        finally:
            browser.close()

if __name__ == "__main__":

        # Connect to WiFi
        if connect_wifi('SIT-Student'):
            # Proceed with SonicWall login
            login_sonicwall(
                url='https://192.168.192.200/sonicui/7/login/#/',
                username='',
                password=''
            )