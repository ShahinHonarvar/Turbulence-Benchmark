
def all_ints_not_div_by_num(numbers):
    num_range = numbers[87:89]
    not_divisible = [i for i in num_range if i % -61 != 0]
    return not_divisible
