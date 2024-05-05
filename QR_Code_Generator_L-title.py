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
    title_font = ImageFont.truetype(font_path, 55)  # Set font size to 55
    title_width, title_height = title_font.getsize(title)

    # Calculate dimensions to ensure the title and QR code fit well
    total_width = max(img.width, title_width)  # Use the wider of the QR code or the title for the total width
    total_height = img.height + title_height + 20  # Total height including space for title

    # Create an image with enough space for the title and QR code
    combined_img = Image.new('RGB', (total_width, total_height), 'white')

    # Calculate the positions for the QR code and the title to center them
    title_y_position = (total_height - img.height - title_height - 20) // 2
    qr_y_position = title_y_position + title_height + 20

    # Paste the QR code into the image, centered horizontally and positioned correctly vertically
    combined_img.paste(img, ((total_width - img.width) // 2, qr_y_position))

    # Add title text to the image, centered horizontally above the QR code
    draw = ImageDraw.Draw(combined_img)
    draw.text(((total_width - title_width) // 2, title_y_position), title, font=title_font, fill="black")

    # Save the result
    combined_img.save(filename)
    print(f"QR code with title '{title}' generated and saved as {filename}")

# Example usage with a hypothetical path to a font file
generate_qr("កម្ពុជា 2AW-4048", "កម្ពុជា 2AW-4048", "2AW-4048.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')
generate_qr("ភ្មំពេញ 2AW-1234", "ភ្មំពេញ 2AW-1234", "2AW-1234.png", 'NotoSerifKhmer-VariableFont_wdth.ttf')
