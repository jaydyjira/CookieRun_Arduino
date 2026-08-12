import cv2

PATH = r"C:\Users\Punna\CookieRun\game_recorded.mov"
cap = cv2.VideoCapture(PATH)
fps = cap.get(cv2.CAP_PROP_FPS)

# Walk the first 600 frames, recording each frame's real presentation timestamp
# and comparing it to the "assume constant fps" estimate.
stamps = []
for i in range(600):
    ok, _ = cap.read()
    if not ok:
        break
    stamps.append(cap.get(cv2.CAP_PROP_POS_MSEC))

deltas = [b - a for a, b in zip(stamps, stamps[1:])]
print(f"gap between consecutive frames: min={min(deltas):.2f} max={max(deltas):.2f} ms")
uniq = sorted({round(d, 1) for d in deltas})
print(f"distinct gap values: {uniq[:12]}{' ...' if len(uniq) > 12 else ''}")

for i in (100, 300, 599):
    if i < len(stamps):
        est = i * 1000 / fps
        print(f"frame {i:4d}: real={stamps[i]:9.2f} ms   idx/fps={est:9.2f} ms   drift={stamps[i]-est:+.2f} ms")
cap.release()

try:
    import matplotlib
    print(f"matplotlib : {matplotlib.__version__}")
except ImportError:
    print("matplotlib : NOT installed")
