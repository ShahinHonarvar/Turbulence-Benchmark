
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    missing_nums = set(range(a + 1, b)) - set(numbers[57:85])
    if len(missing_nums) == 0:
        return ""
    else:
        sum_missing = sum(missing_nums)
        if sum_missing % 2 == 0:
            return hex(sum_missing)[2:]
        else:
            return bin(sum_missing)[2:]
