
def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[91]
    unavailable_nums = set(range(a+1, b)) - set(numbers[13:92])
    sum_unavailable = sum(unavailable_nums)
    if sum_unavailable == 0:
        return ""
    if sum_unavailable % 2 != 0:
        return bin(sum_unavailable)[2:]
    else:
        return hex(sum_unavailable)[2:].upper()
