import pandas as pd
df = pd.read_csv("signal2.csv")
# print(df[df["t_ms"] > 6850][["t_ms","random_boost"]].head(20))
# print(df[df["t_ms"] > 8350][["t_ms","slide"]].head(20))
# print(df[df["t_ms"] > 10150][["t_ms","random_boost"]].head(20))
# print(df[df["t_ms"] > 16000][["t_ms","start"]].head(20))
# print(df[df["t_ms"] > 21300][["t_ms","jump"]].head(20))
print(df[df["t_ms"] > 417000][["t_ms","random_boost"]].head(20))
