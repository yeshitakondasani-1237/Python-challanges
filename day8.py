import random
import pandas as pd
import numpy as np
import math

def simulate_city_data(num_zones=18):
    data = []
    for zone in range(1, num_zones + 1):
        record = {
            "zone": zone,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        data.append(record)
    data[0]["traffic"] = 0
    data[1]["air_quality"] = 280
    data[-1]["traffic"] = 95
    data[-1]["energy"] = 480
    return data

def classify_zone(record):
    if record["air_quality"] > 200 or record["traffic"] > 80:
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30 and record["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"

def calculate_risk_score(record):
    return (record["traffic"] * 0.5 +
            record["air_quality"] * 0.3 +
            record["energy"] * 0.2)

def transform_score(score):
    return math.sqrt(score)

def custom_sort(data, key):
    return sorted(data, key=lambda x: x[key])

def detect_patterns(df):
    threshold = df["risk_score"].mean() + df["risk_score"].std()
    df["multi_factor_risk"] = (
        (df["risk_score"] > threshold) &
        (df["air_quality"].diff().fillna(0) > 0)
    )
    return df, threshold

def check_stability(df):
    return np.var(df["traffic"])

def detect_clusters(df):
    high_risk_zones = df[df["category"] == "High Risk"]["zone"].tolist()
    clusters = []
    temp = []
    for i in range(len(high_risk_zones)):
        if i == 0 or high_risk_zones[i] == high_risk_zones[i-1] + 1:
            temp.append(high_risk_zones[i])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = [high_risk_zones[i]]
    if len(temp) >= 2:
        clusters.append(temp)
    return clusters

city_data = simulate_city_data()

for record in city_data:
    record["category"] = classify_zone(record)
    record["risk_score"] = calculate_risk_score(record)
    record["risk_transformed"] = transform_score(record["risk_score"])

roll_number = 725
if roll_number % 3 == 0:
    random.shuffle(city_data)
else:
    city_data = custom_sort(city_data, "traffic")

df = pd.DataFrame(city_data)

means = np.mean(df[["traffic", "air_quality", "energy"]].values, axis=0)

df, threshold = detect_patterns(df)

sorted_data = sorted(city_data, key=lambda x: x["risk_score"], reverse=True)
top_zones = sorted_data[:3]

risk_tuple = (
    df["risk_score"].max(),
    df["risk_score"].mean(),
    df["risk_score"].min()
)

variance = check_stability(df)

clusters = detect_clusters(df)

if risk_tuple[0] > 400:
    decision = "Critical Emergency"
elif risk_tuple[0] > 300:
    decision = "High Alert"
elif risk_tuple[0] > 200:
    decision = "Moderate Risk"
else:
    decision = "City Stable"

print("SMART CITY DATAFRAME")
print(df)

print("\nMean Values:", means)

print("\nTop 3 Worst Zones:")
for z in top_zones:
    print(z)

print("\nRisk Tuple:", risk_tuple)

print("\nMulti-factor Risk Zones:", df[df["multi_factor_risk"] == True]["zone"].tolist())

print("\nTraffic Variance:", variance)

print("\nCritical Clusters:", clusters)

print("\nFinal Decision:", decision)

print("\nUnique Insight:")
print("A smart city uses integrated real-time data to predict risks, optimize resources, and ensure sustainability while maintaining urban stability.")