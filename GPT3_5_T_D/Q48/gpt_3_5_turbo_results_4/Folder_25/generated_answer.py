
def return_binary_or_hexa(t):
    a = t[37]
    b = t[43]
    missing_nums = [i for i in range(a + 1, b) if i not in t[37:44]]
    if missing_nums == []:
        return ""
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 0:
            return hex(sum_nums)[2:]
        else:
            return bin(sum_nums)[2:]
