f = open("c://code/fun.txt", "r")
f_out = open("c://code/fun_wc.txt", "w")
f_outs = open("c://code/fun_wc.txt", "a")
for line in f:
    tokens = line.split(' ')
    f_out.write("Wordcount is: "+str(len(tokens)) + ' '+"for the line " + ' ' + line)
f_outs.write("Thank you!")
f.close()
f_out.close()
f_outs.close()

