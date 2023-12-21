
def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[84]
    sum_ab = sum(i for i in range(a + 1, b) if i not in numbers[57:85])
    if sum_ab == 0:
        return ""
    elif sum_ab % 2 == 0:
        return hex(sum_ab)[2:]
    else:
        return bin(sum_ab)[2:]
