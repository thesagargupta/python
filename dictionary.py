a = {
    "name" : "sagar",
    "marks" : 100,
    "percent" : 99.99  
}

print(a["marks"])

print(a.items())
print(a.keys())
print(a.values())

a.update({"marks": 200})

print(a)

print(a.get("percent"))