
def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[99]
    subset = set(numbers[86:100])
    sum_num = sum(set(range(a+1, b)) - subset)
    if sum_num % 2 == 1:
        return bin(sum_num)[2:]
    elif sum_num == 0:
        return ""
    else:
        return hex(sum_num)[2:].upper()
