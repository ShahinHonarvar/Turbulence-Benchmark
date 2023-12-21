
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[52]
    range_sum = sum(numbers[a+1: b])
    missing_nums = set(range(a+1, b)) - set(numbers[a+1: b])

    if len(missing_nums) == 0:
        return ""

    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    else:
        return hex(range_sum)[2:]
