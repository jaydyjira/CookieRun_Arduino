import cv2
PATH = r"C:\Users\Punna\CookieRun\game_recorded.mov"

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at:", x, y)

cap = cv2.VideoCapture(PATH)
if not cap.isOpened():
    raise SystemExit("OpenCV could not open the file")
cap.set(cv2.CAP_PROP_POS_MSEC, 11600)

ok, frame = cap.read()
if not ok:
    raise SystemExit("Failed to read frame")
frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
cv2.imshow("frame", frame)
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

# while True:
#     ok, frame = cap.read()
#     frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
#     if not ok:
#         break
#     region_start = frame[905:930, 540:560]
#     grey_start_ = cv2.cvtColor(region_start, cv2.COLOR_BGR2GRAY)
#     cv2.rectangle(frame, (905, 540), (930, 560), (0, 0, 255), 2)
#     cv2.imshow("frame", frame)
#     cv2.setMouseCallback("frame", mouse_callback)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break