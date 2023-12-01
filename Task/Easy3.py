def findmissing (arrr):
    count = []
    for i in range(min(arrr), max(arrr) + 1):          #for i in range(max(arr), min(arr) - 1, -1):
        if i not in arrr:
            count.append(i)
    return count


arr = [1, 2, 5, 4, 6, 3, 9, 10]
print(findmissing(arr))