import cv2
import numpy as np
from PIL import Image

# Define the color in BGR format
yellow = [0, 255, 255]  # BGR for yellow

# Function to get HSV limits for a given color
def get_limits(color):
    # Convert BGR to HSV
    c = np.uint8([[color]])  # Fix: Use np.uint8
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Calculate lower and upper HSV limits
    lowerLimit = np.array([hsvC[0][0][0] - 10, 100, 100])
    upperLimit = np.array([hsvC[0][0][0] + 10, 255, 255])

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
    
    # 2. Convert color to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV limits for yellow
    lowerLimit, upperLimit = get_limits(color=yellow)

    # 3. Create a mask for the color
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    
    # 4. Create a bounding box 

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame =cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    print(bbox)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Detected Color", result)
    
    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
