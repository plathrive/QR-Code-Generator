import os

def listing_path():
    files = sorted([f for f in os.listdir('.') if os.path.isfile(f)])
    return files
