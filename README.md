byteSnap() - Binary/Media File Handler
Purpose
Copies binary or media files through an intermediate .bin file and restores them with their original extension. This utility is useful for handling binary data operations while maintaining file integrity.

Usage
python
byteSnap(old, middle_folder, last_folder)
Example
python
byteSnap(
    old="images\\cat.jpg",
    middle_folder="output\\middle", 
    last_folder="output\\restored"
)
Parameters
old - Path to the original source file

middle_folder - Folder to save the intermediate .bin file

last_folder - Folder to save the final restored file

Key Features
✅ Source file validation - 'old' file must exist

✅ Automatic folder creation - missing directories are created automatically

✅ Consistent naming:

Intermediate file: middlefile.bin

Final restored file: restored + original extension

✅ Supports all binary file types (images, documents, media, etc.)

File Naming Convention
Intermediate file: Always saved as middlefile.bin in the middle_folder

Restored file: Always named restored followed by the original file extension in the last_folder

Example: cat.jpg → middlefile.bin → restored.jpg