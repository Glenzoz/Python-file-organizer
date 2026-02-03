import os
import shutil

# Folder to organize
SOURCE_FOLDER = "files"

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def organize_files():
    if not os.path.exists(SOURCE_FOLDER):
        print("Source folder does not exist.")
        return

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file.lower().endswith(tuple(extensions)):
                    os.makedirs(folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder, file))
                    moved = True
                    break

            if not moved:
                os.makedirs("Others", exist_ok=True)
                shutil.move(file_path, os.path.join("Others", file))

    print("Files organized successfully!")

if __name__ == "__main__":
    organize_files()


