
def return_binary_or_hexa(numbers):
    a = numbers[38]
    b = numbers[81]
    num_range = range(a + 1, b)
    absent_nums = [x for x in num_range if x not in numbers[38:82]]
    sum_absent = sum(absent_nums)
    if sum_absent % 2 == 0:
        return hex(sum_absent)[2:]
    else:
        return bin(sum_absent)[2:] if sum_absent else ""
