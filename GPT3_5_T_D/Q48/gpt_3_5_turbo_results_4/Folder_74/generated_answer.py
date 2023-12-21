
def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    missing_nums = [x for x in range(a + 1, b) if x not in numbers[69:98]]
    if not missing_nums:
        return ""
    sum_missing = sum(missing_nums)
    if sum_missing % 2 == 0:
        return hex(sum_missing)[2:]
    else:
        return bin(sum_missing)[2:]
