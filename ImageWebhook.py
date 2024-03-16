import os
import requests
import tkinter as tk
from tkinter import filedialog

def send_images_to_discord(webhook_url, folder_path):
    valid_extensions = (".jpg", ".jpeg", ".png", ".gif")  # Add more extensions as needed
    image_count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(valid_extensions):  
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as file:
                files = {"file": file}
                requests.post(webhook_url, files=files)
                image_count += 1 
                print(f"Sent: {filename} ({file_path})")
    return image_count

def send_message(webhook_url, message):
    payload = {"content": message}
    requests.post(webhook_url, json=payload)

def select_folder():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory()
    return folder_path

if __name__ == "__main__":
    webhook_url = input("Enter the Discord webhook URL: ")
    folder_path = select_folder()

    if folder_path:
        print("Sending images to Discord...")
        image_count = send_images_to_discord(webhook_url, folder_path)
        print(f"{image_count} Image(s) sent successfully.")
        
        answer = input("Do you want to send the count of uploaded images through the webhook? (yes/no): ")
        if answer.lower() == "yes" or answer.lower() == "y":
            send_message(webhook_url, f"{image_count} Image(s) have been uploaded.")
            print("Image count sent successfully.")
        
    else:
        print("No folder selected.")
