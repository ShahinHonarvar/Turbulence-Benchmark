
def return_binary_or_hexa(numbers_tuple):
    a = numbers_tuple[18]
    b = numbers_tuple[60]
    missing_nums = set(range(a+1, b)) - set(numbers_tuple[18:61])
    sum_missing_nums = sum(missing_nums)

    if sum_missing_nums == 0: 
        return ''
    elif sum_missing_nums % 2 == 0:
        return hex(sum_missing_nums)[2:]
    else:
        return bin(sum_missing_nums)[2:]
