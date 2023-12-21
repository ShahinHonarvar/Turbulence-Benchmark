
def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[51]
    range_sum = sum(range(a+1, b))
    missing_numbers = set(range(a + 1, b)) - set(numbers[21:51])
    if len(missing_numbers) == 0:
        return ''
    if range_sum % 2 == 1: 
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
