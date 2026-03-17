Energy_readings = []
n = int(input("Enter the number of Energy readings: "))

for i in range(n):
    value = int(input("Enter the value of Energy reading: "))
    Energy_readings.append(value)
Classifications = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}

for e in Energy_readings:
    if e < 0:
        Classifications["invalid"].append(e)
    elif e <= 50:
        Classifications["efficient"].append(e)
    elif e <= 150:
        Classifications["moderate"].append(e)
    else:
        Classifications["high"].append(e)

valid = [x for x in Energy_readings if x >= 0]
total = sum(valid)
summary = (
    len(Classifications["efficient"]),
    len(Classifications["moderate"]),
    len(Classifications["high"]),
    len(Classifications["invalid"])
)

Result = ""

if len(Classifications["high"]) > 3:
    Result = "Overconsumption Detected"
elif abs(len(Classifications["efficient"]) - len(Classifications["moderate"])) <= 1:
    Result = "Efficient Campus"
elif total > 600:
    Result = "Energy Waste Detected"
else:
    Result = "Moderate Usage"

print("Categorized Readings:", Classifications)
print("Total Consumption:", total)
print("Number of Buildings:", len(Energy_readings))
print("Summary (Efficient, Moderate, High, Invalid):", summary)
print("Efficiency Result:", Result)