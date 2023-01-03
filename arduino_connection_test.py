ls = open("strings_g3", "r")
llis = ls.readlines()
ls.close()
for index in range(len(llis)):
    llis[index].replace("x", "")
lis = open("new_strings_g3", "w")
for element in llis:
    lis.write(element)
lis.close()

