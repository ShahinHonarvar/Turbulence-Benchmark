
def all_ints_div_by_both_two_nums(ints_list):
    div_ints = [i for i in ints_list[80:201] if i % 10 == 0 and i % 1000 == 0]
    return div_ints
