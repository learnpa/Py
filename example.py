def count_num_and_line(file_path, num):
    numcount = 0
    linecount = 0
    with open(file_path, "r") as f:
        for line in f.readlines():
            linecount += 1
            tokens = line.split(',')
            for token in tokens:
                if num == int(token):
                    numcount += 1
    print("Number of lines in file:", linecount)
    print("Number of occurence of number", '"', num, '"', "in file:", numcount)



def sum_numbers(file_path):
    output_lines = []
    with open(file_path, "r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append("sum: " + str(total) + " | " + line)
    with open(file_path, "w") as f:
        f.writelines(output_lines)


def sum_tokens(tokens):
    sum = 0
    for token in tokens:
        sum += int(token)
    return sum


count_num_and_line("c://code/number.txt", 1)
sum_numbers("c://code//number.txt")
