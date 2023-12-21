
def all_ints_div_by_both_two_nums(lst):
    output = []
    for i in range(93, 95):
        if lst[i] % -53 == 0 and lst[i] % -91 == 0:
            output.append(lst[i])
    return output
