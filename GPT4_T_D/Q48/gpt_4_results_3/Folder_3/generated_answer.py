
def return_binary_or_hexa(numbers):
    a = numbers[56]
    b = numbers[88]
    range_nums = set(range(a + 1, b))
    tuple_nums = set(numbers[56:89])
    sum_nums = sum(range_nums - tuple_nums)
    if not sum_nums:
        return ""
    elif sum_nums % 2 == 1:
        return bin(sum_nums)[2:]
    else:
        return hex(sum_nums)[2:].upper()
