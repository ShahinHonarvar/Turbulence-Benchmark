
def sum_ints_div_by_either_nums(ints):
    return sum(ints[25:95] for i in range(25, 95 + 1) if i % 51 == 0 or i % 77 == 0)
