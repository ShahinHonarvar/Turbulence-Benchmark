
def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    range_nums = set(range(a + 1, b))
    tuple_nums = set(numbers[51:77])
    missing_nums = range_nums - tuple_nums
    if not missing_nums:
        return ''
    else:
        sum_nums = sum(missing_nums)
        if sum_nums % 2 == 1:
            return bin(sum_nums)[2:]
        else:
            return hex(sum_nums)[2:].upper()
