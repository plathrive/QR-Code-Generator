import qrcode

def qr_code_generator(user_input_link, img_filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_input_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_save = img.save(f"{img_filename}.png")