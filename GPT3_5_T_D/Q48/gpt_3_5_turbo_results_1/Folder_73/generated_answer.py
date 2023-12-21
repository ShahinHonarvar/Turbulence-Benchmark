
def return_binary_or_hexa(t):
    a = t[10]
    b = t[76]
    missing_nums = [i for i in range(a+1, b) if i not in t[10:77]]
    if len(missing_nums) == 0:
        return ""
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 1:
            return bin(sum_nums)[2:]
        else:
            return hex(sum_nums)[2:]
