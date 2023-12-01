def findfactorial (facc):
    if facc < 0:
        print("Enter a non negative number: ")
    elif facc == 0 or facc == 1 :
        return 1
    else: 
        return facc * findfactorial(facc - 1)

    


fac = int(input("Enter a number to find factorial: "))
print(findfactorial(fac))



