
def all_ints_div_by_both_two_nums(lst):
    relevant_list = lst[34:82]
    output = [n for n in relevant_list if n%27==0 and n%57==0]
    return output
