import cv2

camera_index = 5
def test_camera_index(camera_index):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Error: Unable to open camera with index {camera_index}")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read frame")
            break

        cv2.imshow(f"Camera {camera_index}", frame)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 0 with the camera index you want to test
    camera_index_to_test = 5
    test_camera_index(camera_index_to_test)
