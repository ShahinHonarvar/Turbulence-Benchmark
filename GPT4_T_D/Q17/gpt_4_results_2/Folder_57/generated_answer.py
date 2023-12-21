
def all_ints_div_by_both_two_nums(num_list):
    dividable = []
    for num in num_list[51:77]:
        if num % -90 == 0 and num % -59 == 0:
            dividable.append(num)
    return dividable
