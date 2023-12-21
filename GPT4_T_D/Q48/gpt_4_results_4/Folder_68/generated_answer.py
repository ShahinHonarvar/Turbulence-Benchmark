
def return_binary_or_hexa(numbers):
    a, b = numbers[0], numbers[9]
    sum_val = 0
    for i in range(a+1, b):
        if i not in numbers:
            sum_val += i
    if sum_val == 0:
        return ''
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
