book = {}
book["tom"] = {
    "name": "Tom", "phone": 9617128383, "Address": "#123, 7th cross lbd, ind"
}
book["jerry"] = {
    "name": "Jerry", "phone": 96167128383, "Address": "#723, 9th cross nbf, ind"
}
# Write dictionary data to json file which is stored as string

import json

s = json.dumps(book)
with open("c://code//book.txt", "w") as f:
    f.write(s)

# read from json file and convert it to dictionary

f = open("c://code//book.txt", "r")
s = f.read()

book = json.loads(s)
for person in book:
    print(book[person])
