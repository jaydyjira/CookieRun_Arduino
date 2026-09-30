import cv2
import csv

PATH = r"C:\Users\Punna\CookieRun\game_recorded2.mp4"
OUT = r"C:\Users\Punna\CookieRun\temp.csv"

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at:", x, y)

cap = cv2.VideoCapture(PATH)
if not cap.isOpened():
    raise SystemExit("OpenCV could not open the file")
start_frame = 0
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", mouse_callback)
with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["frame_idx", "t_ms", "jump", "slide", "start", "random_boost", "relay"])
    idx = 0 + start_frame
    while True:
        t_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        ok, frame = cap.read()
        if not ok:
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5)
        region_jump = frame[550:565, 175:205]
        region_slide = frame[550:565, 1175:1205]
        region_start = frame[540:550, 810:830]
        region_random_boost = frame[535:545, 660:670]
        region_relay = frame[245:260, 685:720]
        gray_jump = cv2.cvtColor(region_jump, cv2.COLOR_BGR2GRAY)
        gray_slide = cv2.cvtColor(region_slide, cv2.COLOR_BGR2GRAY)
        gray_start = cv2.cvtColor(region_start, cv2.COLOR_BGR2GRAY)
        gray_random_boost = cv2.cvtColor(region_random_boost, cv2.COLOR_BGR2GRAY)
        gray_relay = cv2.cvtColor(region_relay, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(frame, (175, 550), (205, 565), (0, 255, 0), 2)
        cv2.rectangle(frame, (1175, 550), (1205, 565), (0, 255, 0), 2)
        cv2.rectangle(frame, (810, 540), (830, 550), (255, 0, 0), 2)
        cv2.rectangle(frame, (660, 535), (670, 545), (255, 255, 0), 2)
        cv2.rectangle(frame, (685, 245), (720, 260), (255, 0, 255), 2)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): # waitkey(1) waits for 1 ms for a key event. If 'q' is pressed, it breaks the loop.
            break
        if key == ord('p'):
            print("Video Paused. Press any key to resume...")
            print(f"Frame {idx} at {t_ms:.2f} ms")
            cv2.waitKey(0)  # Passing 0 pauses indefinitely until another key is pressed
            print("Resuming video...")
        w.writerow([idx, t_ms, gray_jump.mean(), gray_slide.mean(), gray_start.mean(), gray_random_boost.mean(), gray_relay.mean()])
        idx += 1
        if idx % 1000 == 0:
            print(f"frame {idx} at {t_ms:.2f} ms")

cap.release()
cv2.destroyAllWindows()
print("done:", idx, "frames")