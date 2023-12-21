
def return_binary_or_hexa(numbers):
    a = numbers[36]
    b = numbers[54]
    missing_ints = set(range(a+1, b)) - set(numbers[36:55])
    sum_missing_ints = sum(missing_ints)
    if sum_missing_ints % 2 == 1:
        return bin(sum_missing_ints)[2:]
    elif sum_missing_ints % 2 == 0 and sum_missing_ints != 0:
        return hex(sum_missing_ints)[2:].upper()
    else:
        return ""
