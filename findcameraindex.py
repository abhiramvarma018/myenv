import cv2

def find_camera_index():
    for i in range(10):  # Try up to 10 camera indices
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera found at index {i}")
            cap.release()
            return i
    print("No camera found.")
    return None

# Call the function to find the camera index
camera_index = find_camera_index()

# If a camera is found, use it for video capture
if camera_index is not None:
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera Test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
