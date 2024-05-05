import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# List of QR code data that, if found, will color the frame green
allowed_data = ["កម្ពុជា 2AW-4048", "ភ្មំពេញ 2AW-1234"]

def read_qr_from_camera():
    cap = cv2.VideoCapture(0)  # Open the first camera connected to the system
    try:
        while True:
            ret, frame = cap.read()  # Read a frame from the camera
            if not ret:
                print("Failed to grab frame")
                break

            decoded_objects = decode(frame)  # Decode any QR codes in the frame
            for obj in decoded_objects:
                # Decode QR code data and convert from bytes to string
                qr_data = obj.data.decode("utf-8")
                # Determine the color of the rectangle based on whether the data is in the list
                color = (0, 255, 0) if qr_data in allowed_data else (255, 0, 0)

                # Draw on frame using PIL
                pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                draw = ImageDraw.Draw(pil_img)
                font_path = 'NotoSerifKhmer-VariableFont_wdth.ttf'  # Ensure this path is correct
                font = ImageFont.truetype(font_path, 20)
                x, y, w, h = obj.rect
                draw.rectangle([(x, y), (x + w, y + h)], outline=color, width=2)
                draw.text((x, y - 30), qr_data, font=font, fill=color)

                frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

            cv2.imshow("QR Code Scanner", frame)  # Show the frame with overlays
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on pressing 'q'
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

# Start reading QR codes
read_qr_from_camera()
