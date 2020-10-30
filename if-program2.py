indian = ["samosa","Kachori","Cutlet"]
chinese = ["Momos","Manchuri","Noodles"]
italian = ["Sandwitch","Pastry","Pasta"]
cuisine = input("Enter a cuisine of your choice")
if cuisine in indian:
    print("Indian cuisine")
elif cuisine in chinese:
    print("Chinese cuisine")
elif cuisine in italian:
    print("Italian cuisine")
else:
    print("God knows what it is")
