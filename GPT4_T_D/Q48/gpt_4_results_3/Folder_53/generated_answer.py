
def return_binary_or_hexa(numbers):
    a = numbers[200]
    b = numbers[202]
    missing_nums = set(range(a + 1, b)) - set(numbers[200:203])
    result = sum(missing_nums)
    if result == 0:
        return ''
    if result % 2:
        return bin(result)[2:]
    return hex(result)[2:]
