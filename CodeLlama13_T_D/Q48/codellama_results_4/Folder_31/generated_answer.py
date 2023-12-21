
def return_binary_or_hexa(numbers):
    sum = 0
    for i in range(34, 78):
        if numbers[i] not in numbers[33:78]:
            sum += numbers[i]
    if sum % 2 == 1:
        return "{:b}".format(sum)
    else:
        return "{:x}".format(sum).upper()
