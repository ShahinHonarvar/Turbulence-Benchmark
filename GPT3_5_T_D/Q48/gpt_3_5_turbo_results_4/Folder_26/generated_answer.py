
def return_binary_or_hexa(data):
    a = data[68]
    b = data[99]
    total_sum = 0
    
    for num in range(a+1, b):
        if num not in data[68:100]:
            total_sum += num
    
    if total_sum == 0:
        return ""
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    
    return hex(total_sum)[2:]
