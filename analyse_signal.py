import csv, matplotlib.pyplot as plt

t, jump, slide = [], [], []
for r in csv.DictReader(open("signal.csv")):
    t.append(float(r["t_ms"]) / 1000)
    jump.append(float(r["jump"]))
    slide.append(float(r["slide"]))

plt.plot(t, jump, linewidth=0.5, label="jump")
plt.plot(t, slide, linewidth=0.5, label="slide")
plt.xlabel("seconds"); plt.legend(); plt.show()