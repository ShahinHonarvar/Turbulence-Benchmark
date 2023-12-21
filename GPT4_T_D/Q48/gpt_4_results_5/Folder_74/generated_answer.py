
def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    missing_nums = set(range(a + 1, b)) - set(numbers[69:98])
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
