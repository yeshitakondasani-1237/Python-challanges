import random
import math
import copy
import numpy as np
import pandas as pd

random.seed(42)

def generate_data(n=15):
    zones = []
    for i in range(1, n + 1):
        zone = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 300),
                "pollution": random.randint(20, 150),
                "energy": random.randint(100, 500)
            },
            "history": [random.randint(30, 400) for _ in range(5)]
        }
        zones.append(zone)
    return zones

def rotate_data(data):
    return data[3:] + data[:3]

def risk_score(zone):
    t = zone["metrics"]["traffic"]
    p = zone["metrics"]["pollution"]
    e = zone["metrics"]["energy"]
    return math.log(t + p + e)

def custom_score(zone):
    t = zone["metrics"]["traffic"]
    p = zone["metrics"]["pollution"]
    e = zone["metrics"]["energy"]

    avg = sum(zone["history"]) / len(zone["history"])

    score = math.log(t + p + e)
    score *= math.sqrt(p + 1) / math.sqrt(t + 1)
    score += math.log(avg + 1) / 10

    return round(score, 4)

def update_zone(zone):
    zone["metrics"]["traffic"] += random.randint(10, 50)
    zone["metrics"]["pollution"] += random.randint(5, 30)
    zone["metrics"]["energy"] += random.randint(20, 80)
    zone["history"].append(random.randint(100, 500))
    return zone

def create_df(zones):
    data = []

    for z in zones:
        row = {
            "zone": z["zone"],
            "traffic": z["metrics"]["traffic"],
            "pollution": z["metrics"]["pollution"],
            "energy": z["metrics"]["energy"],
            "history_len": len(z["history"]),
            "risk_score": round(risk_score(z), 4),
            "custom_risk": custom_score(z)
        }
        data.append(row)

    return pd.DataFrame(data)

def find_anomalies(df):
    result = set()

    for col in ["traffic", "pollution", "energy", "risk_score"]:
        avg = df[col].mean()
        std = df[col].std()

        zones = df[df[col] > avg + std]["zone"].tolist()

        for z in zones:
            result.add(z)

    return sorted(result)

def correlation(x, y):
    x = np.array(x)
    y = np.array(y)

    x1 = x - x.mean()
    y1 = y - y.mean()

    top = np.sum(x1 * y1)
    bottom = math.sqrt(np.sum(x1 ** 2) * np.sum(y1 ** 2))

    if bottom == 0:
        return 0

    return round(top / bottom, 4)

def find_clusters(df, limit):
    risky = df[df["risk_score"] > limit]["zone"].tolist()

    group = []
    final = []

    for z in df["zone"]:
        if z in risky:
            group.append(z)
        else:
            if len(group) >= 2:
                final.append(group)
            group = []

    if len(group) >= 2:
        final.append(group)

    return final

def stability(df):
    var = np.var(df["risk_score"])

    if var == 0:
        return float("inf")

    return round(1 / var, 6)

def final_result(max_risk, count):
    if max_risk > 7.5 and count >= 5:
        return "CRITICAL FAILURE"
    elif max_risk > 6.5 or count >= 4:
        return "HIGH CORRUPTION RISK"
    elif max_risk > 5.5 or count >= 2:
        return "MODERATE RISK"
    else:
        return "SYSTEM STABLE"

print("=" * 60)
print("ZONE CORRUPTION AND RISK ANALYSIS")
print("=" * 60)

zones = generate_data()
zones = rotate_data(zones)

print("\nZone Order:")
print([z["zone"] for z in zones])

a = zones
b = copy.copy(zones)
c = copy.deepcopy(zones)

print("\nBefore Update:")
print(zones[0])

for zone in zones:
    update_zone(zone)

print("\nAfter Update:")
print(zones[0])

print("\nAssignment Copy Same Object:", a[0] is zones[0])
print("Shallow Copy Shared Inner Object:", b[0]["metrics"] is zones[0]["metrics"])
print("Deep Copy Shared Inner Object:", c[0]["metrics"] is zones[0]["metrics"])

df = create_df(zones)

print("\nData Table:")
print(df.to_string(index=False))

risk = df["risk_score"]
traffic = df["traffic"]
pollution = df["pollution"]

print("\nMean Risk:", round(np.mean(risk), 4))
print("Variance:", round(np.var(risk), 4))
print("Traffic vs Pollution:", correlation(traffic, pollution))
print("Traffic vs Risk:", correlation(traffic, risk))

bad = find_anomalies(df)
print("\nAnomalous Zones:", bad)

limit = np.mean(risk)
groups = find_clusters(df, limit)

print("\nRisky Clusters:", groups)

avg_custom = df["custom_risk"].mean()
high = df[df["custom_risk"] > avg_custom]["zone"].tolist()

print("\nHigh Risk Zones:", high)

max_risk = df["risk_score"].max()
min_risk = df["risk_score"].min()
score = stability(df)

print("\nSummary:")
print((round(max_risk, 4), round(min_risk, 4), score))

print("\nFinal Decision:")
print(final_result(max_risk, len(bad)))