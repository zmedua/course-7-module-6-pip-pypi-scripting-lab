from datetime import datetime
import os
from urllib import request, response
import requests

def generate_log(data):
   
    #log_data = ["User logged in", "User updated profile", "Report exported"]
    
    # STEP 1: Validate input
    # Hint: Check if data is a list
    if not isinstance(data, list):
        raise ValueError("Input data must be a list of log entries.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    # STEP 4: Print a confirmation message with the filename

    print(f"Log written to {filename}")
    return filename
def fetch_data():
    response =requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print(f"Fetched Post Title:",
          post.get("title", "No title found"))
