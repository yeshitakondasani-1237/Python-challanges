weights = []

n = int(input("Enter the number of weights: "))

for i in range(n):
    value = int(input("Enter the value of weight: "))
    weights.append(value)

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

for weight in weights:
    if weight < 0:
        invalid_entries.append(weight)
    elif weight <= 5:
        very_light.append(weight)
    elif weight <= 25:
        normal_load.append(weight)
    elif weight <= 60:
        heavy_load.append(weight)
    else:
        overload.append(weight)

Full_name = input("Enter your full name: ")
L=len(Full_name)
PLI = L % 3
affected_count = 0

if PLI == 0:
    for weight in overload:
        invalid_entries.append(weight)
        affected_count += 1
    overload = []

elif PLI == 1:
    for weight in very_light:
        affected_count += 1
    very_light = []

elif PLI == 2:
    for weight in very_light:
        affected_count += 1
    for weight in overload:
        affected_count += 1
    very_light = []
    overload = []

valid_count = 0

for weight in very_light:
    valid_count += 1
for weight in normal_load:
    valid_count += 1
for weight in heavy_load:
    valid_count += 1
for weight in overload:
    valid_count += 1

print("Name Length :", L)
print("PLI:", PLI)
print("Total Valid Weights:", valid_count)
print("Affected Weights Due to PLI:", affected_count)

print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
