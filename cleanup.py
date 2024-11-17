import os
import time

def clean_up(folder_path, days_old):
    now = time.time()
    cutoff_time = now - (days_old * 86400)  # Calculate cutoff time in seconds
    for root, _, files in os.walk(folder_path):  # Traverse folder and subfolders
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff_time:
                try:
                    os.remove(file_path)  # Delete the file
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# Replace with the folder you want to clean up and days_old
folder = r'C:\Users\dorak\OneDrive\Slike\Snimke zaslona'  # Use raw string to handle backslashes
clean_up(folder, 50)  # Deletes files older than 500 days
