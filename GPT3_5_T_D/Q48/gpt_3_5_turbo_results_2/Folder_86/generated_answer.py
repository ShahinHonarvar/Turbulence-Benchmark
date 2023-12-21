
def return_binary_or_hexa(t):
    a = t[19]
    b = t[32]
    
    missing_nums = []
    for i in range(a + 1, b):
        if i not in t[19:33]:
            missing_nums.append(i)
    
    if len(missing_nums) == 0:
        return ""
    
    total_sum = sum(missing_nums)
    
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]
