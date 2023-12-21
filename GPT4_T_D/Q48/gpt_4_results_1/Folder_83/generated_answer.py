
def return_binary_or_hexa(tup):
    a = tup[90]
    b = tup[200]
    sum_numbers = sum([i for i in range(a+1, b) if i not in tup[90:201]])
    if sum_numbers == 0:
        return ""
    elif sum_numbers % 2:
        return bin(sum_numbers)[2:]
    else:
        return hex(sum_numbers)[2:].upper()
