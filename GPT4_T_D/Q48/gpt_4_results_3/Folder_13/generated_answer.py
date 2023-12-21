
def return_binary_or_hexa(numbers):
    a = numbers[46]
    b = numbers[91]
    absent_numbers = set(range(a+1, b)) - set(numbers[46:92])

    sum_absent_numbers = sum(absent_numbers)
    if sum_absent_numbers == 0:
        return ''
    elif sum_absent_numbers % 2 == 0:
        return hex(sum_absent_numbers)[2:]
    else:
        return bin(sum_absent_numbers)[2:]
