
def return_binary_or_hexa(t: tuple) -> str:
    a = t[0]
    b = t[2]
    missing_nums = []
    
    for i in range(a + 1, b):
        if i not in t:
            missing_nums.append(i)
    
    if len(missing_nums) == 0:
        return ""
    
    sum = 0
    for num in missing_nums:
        sum += num
    
    if sum % 2 == 0:
        return hex(sum)[2:]
    else:
        return bin(sum)[2:]
