
def return_binary_or_hexa(lst):
    a = lst[69]
    b = lst[97]
    sum = 0
    for num in range(a+1, b):
        if num not in lst[69:97]:
            sum += num
    
    if sum == 0:
        return ""
    elif sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:]
