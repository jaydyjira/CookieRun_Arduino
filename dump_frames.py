import cv2

PATH = r"C:\Users\Punna\CookieRun\game_recorded.mov"

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at:", x, y)


cap = cv2.VideoCapture(PATH)
if not cap.isOpened():
    raise SystemExit("OpenCV could not open the file")
cap.set(cv2.CAP_PROP_POS_FRAMES, 600)
while True:
    ok, frame = cap.read()
    if not ok:
        break
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
    region_jump = frame[550:565, 175:205]
    region_slide = frame[550:565, 1175:1205]
    region_start = frame[540:550, 810:830]
    cv2.rectangle(frame, (175, 550), (205, 565), (0, 255, 0), 2)
    cv2.rectangle(frame, (1175, 550), (1205, 565), (0, 255, 0), 2)
    cv2.rectangle(frame, (810, 540), (830, 550), (255, 0, 0), 2)
    gray_jump = cv2.cvtColor(region_jump, cv2.COLOR_BGR2GRAY)
    gray_slide = cv2.cvtColor(region_slide, cv2.COLOR_BGR2GRAY)
    gray_start = cv2.cvtColor(region_start, cv2.COLOR_BGR2GRAY)
    #print(gray_start.mean())
    #print(gray_jump.mean(), gray_slide.mean())
    if gray_jump.mean() < 100:
        print("Jump", cap.get(cv2.CAP_PROP_POS_MSEC), cap.get(cv2.CAP_PROP_POS_FRAMES))
    if gray_slide.mean() < 100:
        print("Slide", cap.get(cv2.CAP_PROP_POS_MSEC), cap.get(cv2.CAP_PROP_POS_FRAMES))
    if gray_start.mean() < 80:
        print("Start", cap.get(cv2.CAP_PROP_POS_MSEC), cap.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break