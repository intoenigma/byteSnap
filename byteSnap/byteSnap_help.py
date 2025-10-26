
def byteSnap_help():
    print("""
    === byteSnap() Help Page ===
    Purpose:
        Organizes image files by checking, creating folders, and copying files.

    Usage:
        byteSnap(old, middle, last)

    Example:
        byteSnap("images/cat.jpg", "output/middle", "output/last")

    Parameters:
        old     -> Path to existing image file (string)
        middle  -> Folder path to create (string)
        last    -> Folder path to create (string)

    Notes:
        - 'old' file must exist
        - 'middle' and 'last' folders will be created if missing
        - Modify function to move, rename, or resize files if needed
    ============================
    """)
    print("Thank You")