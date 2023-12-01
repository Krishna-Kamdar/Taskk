def sumofpairs (kk, arrr):
    index = len(arrr)
    pairs = []
    for i in range(index):
        for j in range(i + 1, index):
            if arrr[i] + arrr[j] == kk:
                pairs.append((arrr[i], arrr[j]))
    return pairs




arr = [1, 3, -4, 2, 2]
k = 4
result = sumofpairs(k, arr)
print(f"Pairs are: {result} = Sum of Pairs {k}")