
def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[315:935]:
        if num % -897 == 0 or num % -556 == 0:
            total += num
    return total
