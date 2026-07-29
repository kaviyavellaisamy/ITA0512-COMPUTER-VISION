import cv2

# Read video
cap = cv2.VideoCapture(r"C:\Users\Kaviya V\Downloads\video.webm")

if not cap.isOpened():
    print("Cannot open video")
    exit()

print("Choose Playback Speed")
print("1 - Slow Motion")
print("2 - Normal")
print("3 - Fast Motion")

choice = input("Enter your choice: ")

if choice == "1":
    delay = 100      # Slow Motion
elif choice == "3":
    delay = 10       # Fast Motion
else:
    delay = 30       # Normal Speed

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
