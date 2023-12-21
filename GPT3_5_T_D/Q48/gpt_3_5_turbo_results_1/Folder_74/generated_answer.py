
def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    missing_nums = set(range(a + 1, b)) - set(numbers[70:97])
    sum_missing = sum(missing_nums)
    
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:]
