
def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    missing_nums = set(range(a + 1, b)) - set(numbers[16: 88])
    sum_nums = sum(missing_nums)
    if sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
