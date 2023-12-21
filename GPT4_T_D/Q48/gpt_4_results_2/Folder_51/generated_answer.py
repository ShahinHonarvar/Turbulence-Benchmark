
def return_binary_or_hexa(t):
    a = t[6]
    b = t[9]
    required_nums = set(range(a + 1, b))
    given_nums = set(t[6:10])
    missing_nums = required_nums - given_nums
    sum_missing_nums = sum(missing_nums)
    if sum_missing_nums % 2 == 1:
        return bin(sum_missing_nums)[2:]
    else:
        return hex(sum_missing_nums)[2:].upper()
