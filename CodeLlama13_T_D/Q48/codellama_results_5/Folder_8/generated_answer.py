
def return_binary_or_hexa(tup):
    a, b = tup[45], tup[48]
    sum = 0
    for i in range(a+1, b-1+1):
        if i not in tup:
            sum += 1
    return "" if sum == 0 else "{:x}".format(sum) if sum % 2 != 0 else bin(sum)[2:]
