import qrcode

def generate_qr_code(data, filename):
    """
    Generate a QR code for the given data and save it as an image file.

    Parameters:
        data (str): The data to be encoded in the QR code.
        filename (str): The name of the image file to be saved (e.g., 'my_qrcode.png').

    Returns:
        None
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


if __name__ == "__main__":
    data_to_encode = input("Enter the data to encode as a QR code: ")
    output_filename = input("Enter the name of the output image file (e.g., 'my_qrcode.png'): ")

    generate_qr_code(data_to_encode, output_filename)
    print(f"QR code saved as '{output_filename}'")
