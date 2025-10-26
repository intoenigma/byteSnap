import os


def byteSnap(old: str, middle_folder: str, last_folder: str) -> None:
    """
    Copies a file to an intermediate '.bin' file, then restores it with the name 'restored'
    while keeping the original file extension.

    Parameters:
        old           -> Path to the original file.
        middle_folder -> Folder to save the intermediate .bin file.
        last_folder   -> Folder to save the final restored file.
    """

    print("Process Started ✅")

    # Check if source file exists
    if not os.path.exists(old):
        print(f"Error: Source file '{old}' does not exist ❌")
        return

    # Ensure middle and last folders exist
    os.makedirs(middle_folder, exist_ok=True)
    os.makedirs(last_folder, exist_ok=True)

    # Fixed middle file name
    middle = os.path.join(middle_folder, "middlefile.bin")

    # Extract original file extension
    _, ext = os.path.splitext(old)
    last = os.path.join(last_folder, f"restored{ext}")

    # Read the original file
    with open(old, "rb") as file:
        data = file.read()
    print("Reading the original file ✅")

    # Write to middle file
    with open(middle, "wb") as file:
        file.write(data)
    print(f"Middle file '{middle}' written ✅")

    # Read from middle file
    with open(middle, "rb") as file:
        binary_data = file.read()
    print("Reading the middle file ✅")

    # Write to final file
    with open(last, "wb") as file:
        file.write(binary_data)
    print(f"Final file '{last}' written ✅")

    print("Process Completed Successfully ✅")
