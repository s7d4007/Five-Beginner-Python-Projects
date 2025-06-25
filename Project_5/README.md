# 🗂️ File Organizer (Based on File Extensions)

A simple Python script that automatically organizes files in a given directory by sorting them into folders based on their file extensions. Perfect for cleaning up messy Downloads or Desktop folders!

---

## 📁 How It Works

The script scans a folder, identifies each file’s extension, and moves the file into a subfolder (like `Images/`, `Documents/`, `Music/`, etc.) based on a predefined mapping.

### 🔍 File Types Supported

- **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- **Documents:** `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`
- **Videos:** `.mp4`, `.mkv`, `.mov`, `.avi`
- **Music:** `.mp3`, `.wav`, `.aac`
- **Archives:** `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Scripts:** `.py`, `.js`, `.sh`, `.bat`
- **Others:** Files that don’t match any category above

---

## 🛠️ Installation & Setup

1. **Clone the Repository**
    ```bash
    git clone https://github.com/s7d4007/file-organizer.git
    cd file-organizer
    ```

2. **Make sure Python is installed**
    ```bash
    python --version
    ```

---

## 🚀 Usage

Run the script from the terminal or any IDE:

```bash
python file_organizer.py
```

---

## ✅ Features

- Organizes files into folders based on extensions
- Automatically creates folders if they don’t exist
- Skips already organized folders
- Lightweight and easy to customize

---

## 📄 License

This project is licensed under the MIT License.
