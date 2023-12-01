def revstring(stringg):
    index = len(stringg)
    s = ''
    while index > 0:
        s += stringg[index - 1]
        index = index - 1
    return s


string = input("Enter the number: ")
print(revstring(string))