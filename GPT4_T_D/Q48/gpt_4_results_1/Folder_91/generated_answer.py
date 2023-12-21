
def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[6]
    sum_absent = sum(set(range(a+1, b)) - set(numbers[0:7]))
    if sum_absent == 0:
        return ''
    elif sum_absent % 2 == 0:
        return hex(sum_absent)[2:]
    else:
        return bin(sum_absent)[2:]
