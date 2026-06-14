import os
from qr_code import qr_code_generator
from path import listing_path

if __name__ == "__main__":
    print("=======================")
    print("   QR Code Generator   ")
    print("=======================")
    user_input_link = input("Enter your link: ")
    img_filename = input("Enter the filename: ")
    qr_code_generator(user_input_link, img_filename)
    print("=======================")
    for file in listing_path():
        if file == (f"{img_filename}.png"):
            print("Image generate successfully!")
            print("To view, look at your directories.")
            print("Listing current directories:")
            print("-----------------------")
            for file in listing_path():
                print(file)
            print("-----------------------")

