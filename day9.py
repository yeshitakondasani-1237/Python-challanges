import copy

def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def replicate_data(data):
    assigned = data
    shallow = copy.copy(data)
    deep = copy.deepcopy(data)
    return assigned, shallow, deep

def modify_data(data, roll):
    for user in data:
        if roll % 2 != 0:
            if user["data"]["files"]:
                user["data"]["files"].pop()
        else:
            user["data"]["files"].append("new.txt")
        user["data"]["usage"] += 100

def check_integrity(original, assigned, shallow, deep):
    leakage = 0
    safe = 0

    if original != generate_data():
        leakage += 1
    else:
        safe += 1

    if deep == generate_data():
        safe += 1

    overlap = set()
    for i in range(len(original)):
        o = set(original[i]["data"]["files"])
        d = set(deep[i]["data"]["files"])
        overlap.update(o.intersection(d))

    return leakage, safe, len(overlap)

original = generate_data()

assigned, shallow, deep = replicate_data(original)

before = copy.deepcopy(original)

roll_number = 725

modify_data(assigned, roll_number)
modify_data(shallow, roll_number)

after = original

result = check_integrity(original, assigned, shallow, deep)

print("=== BEFORE ===")
print(before)

print("\n=== AFTER (ORIGINAL) ===")
print(after)

print("\n=== ASSIGNMENT ===")
print(assigned)

print("\n=== SHALLOW COPY ===")
print(shallow)

print("\n=== DEEP COPY ===")
print(deep)

print("\n=== INTEGRITY REPORT ===")
print("Leakage, Safe, Overlap:", result)