import qrcode

def generate_qr(data, filename='qr.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

# Example usage
generate_qr("កម្ពុជា 2AW-4048","កម្ពុជា 2AW-4048"+".png")
generate_qr("ភ្មំពេញ 2AW-1234","ភ្មំពេញ 2AW-1234"+".png")
