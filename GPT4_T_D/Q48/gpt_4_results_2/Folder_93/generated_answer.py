
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    sum_of_absent_nums = sum(set(range(a+1, b)) - set(numbers[57:85]))
    if sum_of_absent_nums % 2 == 0:
        return hex(sum_of_absent_nums)[2:].upper()
    else:
        return bin(sum_of_absent_nums)[2:]
