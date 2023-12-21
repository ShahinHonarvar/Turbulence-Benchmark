
def return_binary_or_hexa(tup):
    a = tup[10]
    b = tup[12]
    
    nums = set(tup[a+1:b])
    total_sum = 0
    
    for num in range(a+1, b):
        if num not in nums:
            total_sum += num
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
