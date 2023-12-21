
def return_binary_or_hexa(numbers):
    a = numbers[3]
    b = numbers[9]
    sum_val = sum(set(range(a+1, b)) - set(numbers[3:10]))
    if sum_val == 0:
        return ""
    elif sum_val % 2 == 0:
        return hex(sum_val)[2:]
    else:
        return bin(sum_val)[2:]
