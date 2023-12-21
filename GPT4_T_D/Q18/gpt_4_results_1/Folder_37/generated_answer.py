
def sum_ints_div_by_either_nums(int_list):
    res = [i for i in int_list[2:8] if i % -1 == 0 or i % -7 == 0]
    return sum(res) if res else 0
