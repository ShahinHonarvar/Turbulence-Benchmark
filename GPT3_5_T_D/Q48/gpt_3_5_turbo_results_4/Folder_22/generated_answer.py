
def return_binary_or_hexa(numbers):
    a = numbers[40]
    b = numbers[200]
    range_sum = sum(numbers[a + 1:b])
    missing_nums = [n for n in range(a + 1, b) if n not in numbers[40:200]]
    
    if len(missing_nums) == 0:
        return ""
    elif range_sum % 2 == 1:
        return "{0:b}".format(range_sum)
    else:
        return "{0:X}".format(range_sum)
