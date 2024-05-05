from PIL import Image, ImageDraw, ImageFont
import qrcode


def generate_qr(data, title, filename='qr.png', font_path='NotoSerifKhmer-VariableFont_wdth.ttf'):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white').convert('RGB')

    # Load a font that supports Khmer script
    title_font = ImageFont.truetype(font_path, 24)  # Adjust font size as needed
    title_width, title_height = title_font.getsize(title)

    # Create an image with space for title
    total_height = img.height + title_height + 10
    combined_img = Image.new('RGB', (img.width, total_height), 'white')
    combined_img.paste(img, (0, title_height + 10))

    # Add title text to image
    draw = ImageDraw.Draw(combined_img)
    draw.text(((img.width - title_width) / 2, 0), title, font=title_font, fill="black")

    # Save the result
    combined_img.save(filename)
    print(f"QR code with title '{title}' generated and saved as {filename}")


# Example usage with a hypothetical path to a font file
generate_qr("កម្ពុជា 2AW-4048", "កម្ពុជា 2AW-4048", "កម្ពុជា 2AW-4048.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')
generate_qr("ភ្មំពេញ 2AW-1234", "ភ្មំពេញ 2AW-1234", "ភ្មំពេញ 2AW-1234.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')

generate_qr("ភ្មំពេញ 2AB-9999", "ភ្មំពេញ 2AB-9999", "ភ្មំពេញ 2AB-9999.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')
generate_qr("ភ្មំពេញ 2AB-7777", "ភ្មំពេញ 2AB-7777", "ភ្មំពេញ 2AB-7777.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')
