
def sum_ints_div_by_either_nums(ints):
    sum_ints = 0
    for num in ints[42:88]:
        if num%(-90) == 0 or num%(-74) == 0:
            sum_ints += num
    return sum_ints if sum_ints > 0 else 0
