
def return_binary_or_hexa(numbers):
    a = numbers[2]
    b = numbers[8]

    absent_numbers = set(range(a+1, b)) - set(numbers[2:9])
    sum_absent_numbers = sum(absent_numbers)

    if sum_absent_numbers == 0:
        return ''
    elif sum_absent_numbers % 2 == 1:
        return bin(sum_absent_numbers)[2:]
    else:
        return hex(sum_absent_numbers)[2:].upper()
