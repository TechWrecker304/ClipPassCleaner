import pyperclip
import time
import re

def check_clipboard_for_password(clipboard_content):
    # Regular expression pattern to detect possible passwords
    # This example checks for at least 8 characters, containing both letters and numbers
    password_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
    
    return bool(password_pattern.match(clipboard_content))

def main():
    last_checked = ""
    
    while True:
        clipboard_content = pyperclip.paste()
        
        if clipboard_content != last_checked:
            last_checked = clipboard_content
            
            if check_clipboard_for_password(clipboard_content):
                print("Potential password detected. Clearing clipboard in 30 seconds...")
                
                # Wait for 30 seconds before clearing the clipboard
                time.sleep(10)
                
                pyperclip.copy("")
                print("Clipboard cleared.")
                
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()
