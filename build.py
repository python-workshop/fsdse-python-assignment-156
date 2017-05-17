def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x) / 2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

A = [1,5,4,8,96,5,55]
print(msort(A))