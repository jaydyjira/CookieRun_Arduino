import cv2

PATH = r"C:\Users\Punna\CookieRun\ScreenRecording_08-11-2569 22-05-26_1.mov"

cap = cv2.VideoCapture(PATH)
if not cap.isOpened():
    raise SystemExit("OpenCV could not open the file (codec problem?)")

fps    = cap.get(cv2.CAP_PROP_FPS)
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
w      = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h      = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
codec  = "".join(chr((fourcc >> 8 * i) & 0xFF) for i in range(4))

print(f"resolution : {w} x {h}")
print(f"fps        : {fps}")
print(f"frames     : {frames}")
print(f"duration   : {frames / fps:.2f} s  ({frames / fps / 60:.2f} min)")
print(f"codec      : {codec}")
print(f"ms/frame   : {1000 / fps:.2f}")

ok, frame = cap.read()
print(f"first read : {'OK' if ok else 'FAILED'}  shape={None if not ok else frame.shape}")
cap.release()
