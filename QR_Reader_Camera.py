import cv2
from pyzbar.pyzbar import decode


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
                print("Data:", obj.data.decode("utf-8"))  # Print decoded data

            cv2.imshow("QR Code Scanner", frame)  # Show the frame
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit on pressing 'q'
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


# Start reading QR codes
read_qr_from_camera()
