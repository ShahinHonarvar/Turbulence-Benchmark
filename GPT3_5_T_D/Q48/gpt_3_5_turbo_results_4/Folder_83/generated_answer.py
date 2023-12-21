
def return_binary_or_hexa(lst):
    a = lst[90]
    b = lst[200]
    total_sum = sum([i for i in range(a+1, b) if i not in lst[90:201]])
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
