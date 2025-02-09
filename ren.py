import os

def rename_files_in_folder(folder_path):
    try:
        # Get a sorted list of all files in the folder
        files = sorted(f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)))
        
        # Check if the folder is empty
        if not files:
            print("No files found in the folder.")
            return

        # Rename files sequentially
        for index, file in enumerate(files, start=1):
            # Extract the file extension
            file_extension = os.path.splitext(file)[1]
            # Create the new file name with zero-padded numbering
            new_name = f"{index:04}{file_extension}"
            # Get full paths for renaming
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, new_name)
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {file} -> {new_name}")

        print("All files have been renamed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the folder path
folder_path = "songs"  # Replace with the actual folder path

# Call the function
rename_files_in_folder(folder_path)
