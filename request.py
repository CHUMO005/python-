import os
import requests
from urllib.parse import urlparse
from pathlib import Path

def get_image_filename(url):
    """Extracts a filename from the image URL."""
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path) or "downloaded_image.jpg"

def download_image(url, save_path):
    """Attempts to download the image and save it to the specified path."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f" Image saved to: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f" Failed to download image: {e}")

def main():
    url = input("Enter the image URL: ").strip()
    if not url:
        print(" No URL provided. Exiting.")
        return

    # Create directory if it doesn't exist
    directory = Path("Fetched_Images")
    directory.mkdir(exist_ok=True)

    # Determine filename and full path
    filename = get_image_filename(url)
    save_path = directory / filename

    # Download and save image
    download_image(url, save_path)

if __name__ == "__main__":
    main()
