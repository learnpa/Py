# demo for loop

exp=[1000,2000,1500,4500,1200]
total=0
for i in range(len(exp)):
    print("Month",(i+1),"Expense",exp[i])
    total = total + exp[i]
print("Total expense is", total)

for i in range(1,6):
    if i%2 == 0:
        continue
    else:
        print(i*i)

# while loop

i=0
while (i<5):
    print(i)
    i=i+1







