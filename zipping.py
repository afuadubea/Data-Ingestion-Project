import zipfile
import os

# Define the folder containing the CSV files and the zip file name
folder = 'your_folder_path'
zip_file = 'zip_file_name.zip'  # Ensure the zip file has a .zip extension

try:
    # Check if the folder exists
    if not os.path.exists(folder):
        raise FileNotFoundError(f'The folder {folder} does not exist')

    # Get the list of CSV files
    csv_files = [file for file in os.listdir(folder) if file.endswith('.csv')]

    # Check if there are any CSV files
    if not csv_files:
        raise FileNotFoundError('No CSV files found in the folder')

    # Create the zip file path
    zip_file_path = os.path.join(folder, zip_file)

    # Create a new zip file and add the CSV files to it
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_name in csv_files:
            file_path = os.path.join(folder, file_name)
            print(f'Adding {file_path} to zip file')  # Debugging line
            zipf.write(file_path, arcname=file_name)

    print(f'CSV files in {folder} have been zipped into {zip_file_path}')

except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(f'Permission error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
