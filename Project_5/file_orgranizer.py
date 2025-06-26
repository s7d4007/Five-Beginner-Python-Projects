import os
import shutil

#Creating a dictionary for categorizing file extension. Don't worry it is not as hard as it seems

Extensions = {
    'Images' : ['.jpg', '.jpeg', '.gif', '.png','.webp','.bmp'],
    'Documents' : ['.docx','.xlsx','.pptx','.txt','.pdf','.doc'],
    'Videos' : ['.mp4','.mkv','.mov','.avi'],
    'Music' : ['.mp3','.wav','.aac'],
    'Archives' : ['.zip','.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': [] #For Uncategorized files
}

def get_folder_name(extension):
    for folder, extensions in Extensions.items():
        if extension in extensions:
            return folder
    return 'Others'
    
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        #Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        folder_name = get_folder_name(ext)
        folder_path = os.path.join(directory, folder_name)

        os.makedirs(folder_path, exist_ok=True)

        new_file_path = os.path.join(folder_path, filename)
        shutil.move(file_path, new_file_path)
        
        print(f"Moved: {filename} --> {folder_name}/")
        
#Main Function
if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ").strip()
    if os.path.isdir(folder_to_organize):
        organize_files(folder_to_organize)
        print("✅ Organizing completed!")
    else:
        print("❌ Invalid folder path.")