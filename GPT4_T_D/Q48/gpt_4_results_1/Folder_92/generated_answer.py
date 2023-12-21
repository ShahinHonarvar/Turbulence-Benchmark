
def return_binary_or_hexa(t):
    a = t[0]
    b = t[2]
    missing_nums = [i for i in range(a + 1, b) if i not in t[1:3]]
    if not missing_nums:
        return ""
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 0:
            return hex(sum_nums)[2:]
        else:
            return bin(sum_nums)[2:]
