
def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    absent_numbers = set(range(a+1, b)) - set(numbers[27:97])
    sum_absent = sum(absent_numbers)
    if sum_absent == 0:
        return ''
    elif sum_absent % 2 == 0:
        return hex(sum_absent)[2:]
    else:
        return bin(sum_absent)[2:]
