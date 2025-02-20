import cv2
import numpy as np
from PIL import Image

# Define the color in BGR format (OpenCV uses BGR)
color = [0, 255, 255]

# Function to get BGR limits for a given color
def get_limits(color):
    # Expand the range to improve detection
    lowerLimit = np.array([0, 150, 150])  
    upperLimit = np.array([100, 255, 255])  

    # Ensure limits are within valid range (0 to 255)
    lowerLimit = np.clip(lowerLimit, 0, 255)
    upperLimit = np.clip(upperLimit, 0, 255)

    return lowerLimit, upperLimit

# Initialize the camera capture object (0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # 1. Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    # Get BGR limits for yellow
    lowerLimit, upperLimit = get_limits(color=color)

    # 2. Create a mask for the color in BGR
    mask = cv2.inRange(frame, lowerLimit, upperLimit)
    
    # 3. Create a bounding box 
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 5)

    print(bbox)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Detected Color", result)
    
    # Break the loop on pressing 'q'

    key = cv2.waitKey(1) & 0xFF 
    
    if key == ord('q'): 
        break
    if key == ord('c'):
        cv2.imwrite("captured_image.jpg", frame)
        print("Image is saved")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
