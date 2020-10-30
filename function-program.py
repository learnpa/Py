
tom_list =[1,2,3,4,5]
joe_list =[2,1,5,5,4]

def calculate_exp(exp):
    total=0
    for i in exp:
        total=total+i
    return total

tom_exp= calculate_exp(tom_list)
joe_exp= calculate_exp(joe_list)

print("tom's expense", tom_exp)
print("joe's expense", joe_exp)

