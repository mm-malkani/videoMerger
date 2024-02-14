import shutil
import os

def extract_zip(zip_file_path, extract_destination):
    try:
        with open(zip_file_path, 'rb') as zip_file:
            shutil.unpack_archive(zip_file_path, extract_destination)
            print(f"Successfully extracted {zip_file_path} to {extract_destination}")
    except Exception as e:
        print(f"Error extracting {zip_file_path}: {e}")

if __name__ == "__main__":
    # Replace these paths with your actual file and destination paths
    zip_file_path =  "" #PATH OF FILE TO BE EXTRACTED
    extract_destination = "" #PATH OF FILE WHERE IT IS EXTRACTED
    # Check if the file and destination exist
    if os.path.exists(zip_file_path) and os.path.exists(extract_destination):
        # Ensure that the script has permission to access the directories
        if os.access(zip_file_path, os.R_OK) and os.access(extract_destination, os.W_OK):
            extract_zip(zip_file_path, extract_destination)
        else:
            print("Permission denied. Check file and destination directory permissions.")
    else:
        print("File or destination directory not found.")
