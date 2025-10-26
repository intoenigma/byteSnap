🧩 byteSnap — Binary/Media File Handler

byteSnap is a simple and reliable Python utility for copying and restoring binary or media files while maintaining full data integrity.
It works by saving an intermediate .bin file and then reconstructing the original file from that binary snapshot.

📘 Purpose

byteSnap allows you to safely handle and transfer binary data (such as images, audio, video, or documents) using an intermediate .bin file.
This can be useful for:

Data transformation pipelines

File integrity validation

Temporary binary storage

Handling non-text data in automated workflows

⚙️ Usage
python byteSnap(old, middle_folder, last_folder)

🧠 Example
python byteSnap(
    old="images/cat.jpg",
    middle_folder="output/middle",
    last_folder="output/restored"
)

📂 Parameters
Parameter	Description
old	Path to the original source file (must exist)
middle_folder	Folder to save the intermediate .bin file
last_folder	Folder to save the final restored file
🚀 Key Features

✅ Source file validation — Ensures the input (old) file exists before processing.
✅ Automatic folder creation — Creates missing directories in middle_folder and last_folder automatically.
✅ Consistent file naming — Standardized intermediate and restored file names.
✅ Universal binary support — Works with all binary file types (images, documents, audio, video, etc.).

🧾 File Naming Convention
Stage	File Name	Location
Intermediate File	middlefile.bin	Saved in middle_folder
Restored File	restored + original extension	Saved in last_folder
Example:
Original:  cat.jpg
Intermediate:  middlefile.bin
Restored:  restored.jpg

🪄 How It Works

Read the source file in binary mode (rb).

Write the data into middlefile.bin inside the middle_folder.

Read the .bin file back and reconstruct the original file data.

Save the final output as restored.<original_extension> inside the last_folder.

📋 Example Workflow

Input:

images/cat.jpg


Intermediate Output:

output/middle/middlefile.bin


Final Restored Output:

output/restored/restored.jpg

🧰 Requirements

Python 3.7+

No external dependencies (uses built-in libraries)

💡 Notes

This utility is designed for binary-safe operations — no data loss or encoding issues.

All file I/O operations are performed using rb and wb modes.

Directory creation is handled automatically via os.makedirs().