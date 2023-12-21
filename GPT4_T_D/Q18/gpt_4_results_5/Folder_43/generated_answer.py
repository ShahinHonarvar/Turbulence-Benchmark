
def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 86:
        return 0
    else:
        relevant_ints = int_list[57:86]
        sum_divisibles = sum(i for i in relevant_ints if i % -77 == 0 or i % -32 == 0)
        return sum_divisibles
