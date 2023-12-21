
def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    sum_nums = sum(set(range(a + 1, b)) - set(numbers[70:99]))

    if sum_nums == 0:
        return ""
    elif sum_nums % 2 == 0:
        return hex(sum_nums)[2:]
    else:
        return bin(sum_nums)[2:]
