d = {"tom": 123456, "Jerry": 3427733, "poppy": 4545454}
for key in d:
    print("Key is", key, "Value is", d[key])

print(d["tom"])
del d["tom"]
print (d[key])
if "tom" in d:
    print("True")
else:
    print("false")