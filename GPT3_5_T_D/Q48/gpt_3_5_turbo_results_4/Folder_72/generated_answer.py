
def return_binary_or_hexa(t):
    a = t[13]
    b = t[70]
    missing_nums = []
    for i in range(a+1, b):
        if i not in t[14:70]:
            missing_nums.append(i)
    if not missing_nums:
        return ""
    total = sum(missing_nums)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()
