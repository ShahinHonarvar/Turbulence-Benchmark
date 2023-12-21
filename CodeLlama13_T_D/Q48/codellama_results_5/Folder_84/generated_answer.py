
def return_binary_or_hexa(numbers):
    a, b = numbers[32], numbers[44]
    sum_of_missing = 0
    for i in range(a+1, b-1):
        if i not in numbers:
            sum_of_missing += i
    if sum_of_missing % 2 == 0:
        return hex(sum_of_missing)
    else:
        return bin(sum_of_missing)[2:]
