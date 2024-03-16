import os
import requests
import tkinter as tk
from tkinter import filedialog

def send_images_to_discord(webhook_url, folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Change file extensions as needed
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as file:
                files = {"file": file}
                requests.post(webhook_url, files=files)
                print(f"Sent: {filename} ({file_path})")

def select_folder():
    root = tk.Tk()
    root.withdraw() 

    folder_path = filedialog.askdirectory()
    return folder_path

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL: ")
    print("Set folder directory: ")
    folder_path = select_folder()
    print(f"Folder path set to {folder_path}")
    print("---------------------------------")

    if folder_path:
        print("Sending images to Discord...")
        send_images_to_discord(webhook_url, folder_path)
        print("Images sent successfully.")
    else:
        print("No folder selected.")
