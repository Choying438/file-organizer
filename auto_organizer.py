import os
import shutil
from datetime import datetime

# RGB Color Codes
class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GOLD = '\033[38;5;220m'
    PINK = '\033[38;5;213m'
    GREEN = '\033[38;5;84m'
    RED = '\033[38;5;203m'
    BLUE = '\033[38;5;75m'
    RESET = '\033[0m'

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".flac", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"]
}

def print_header():
    print(f"{Colors.PINK}╔{'═'*50}╗{Colors.RESET}")
    print(f"{Colors.PINK}║{Colors.GOLD}{'FILE ORGANIZER'.center(50)}{Colors.PINK}║{Colors.RESET}")
    print(f"{Colors.PINK}║{Colors.CYAN}{'Created by Choying'.center(50)}{Colors.PINK}║{Colors.RESET}")
    print(f"{Colors.PINK}╚{'═'*50}╝{Colors.RESET}")

def organize_files():
    print_header()
    
    # Get folder paths
    source = input(f"{Colors.CYAN}Enter source folder path: {Colors.RESET}").strip()
    dest = input(f"{Colors.CYAN}Enter destination folder path: {Colors.RESET}").strip()

    # Verify folders exist
    if not os.path.exists(source):
        print(f"\n{Colors.RED}✗ Error: Source folder doesn't exist!{Colors.RESET}")
        return

    os.makedirs(dest, exist_ok=True)
    moved_files = 0
    errors = 0

    print(f"\n{Colors.GOLD}Starting organization...{Colors.RESET}")
    
    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)
        dest_path = None
        
        try:
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                category = "Other"
                
                # Find the right category
                for cat, exts in FILE_TYPES.items():
                    if ext in exts:
                        category = cat
                        break
                
                # Create destination folder
                dest_folder = os.path.join(dest, category)
                os.makedirs(dest_folder, exist_ok=True)
                
                # Set destination path
                dest_path = os.path.join(dest_folder, filename)
                
                # Perform the move
                shutil.move(file_path, dest_path)
                moved_files += 1
                print(f"{Colors.GREEN}✓ Moved {filename} to {category}{Colors.RESET}")
                
        except Exception as e:
            errors += 1
            print(f"{Colors.RED}✗ Failed to move {filename}: {e}{Colors.RESET}")

    # Final report
    print(f"\n{Colors.GOLD}=== Results ==={Colors.RESET}")
    print(f"{Colors.GREEN}✓ Successfully moved: {moved_files} files{Colors.RESET}")
    print(f"{Colors.RED}✗ Errors encountered: {errors}{Colors.RESET}")
    
    if moved_files == 0 and errors == 0:
        print(f"{Colors.RED}No files found in source folder!{Colors.RESET}")

if __name__ == "__main__":
    organize_files()
    input(f"\n{Colors.GOLD}Press Enter to exit...{Colors.RESET}")