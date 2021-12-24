str1 = input('str1 = ')
input_file = input('input_file = ')
output_file = input('output_file = ')

res_list = []

with open(input_file,'r') as f:
    for line in f:
        line = line.rstrip('\n')
        hamming = 0
        if len(str1) == len(line):
            for j in range(len(str1)):
                if str1[j] != line[j]:
                    hamming += 1
            res_list.append([hamming, line])
        else:
            line = f"{line} - не совпадают длины"
            res_list.append([-1, line])

res_list.sort()
with open(output_file,'w') as f:
    s = f"Введенная строка: {str1}\n"
    f.write(s)
    for elem in res_list:
        s = f"{str(elem[0])} {elem[1]}\n"
        f.write(s)