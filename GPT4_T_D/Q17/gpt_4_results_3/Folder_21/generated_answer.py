
def all_ints_div_by_both_two_nums(num_list):
    result = []
    for num in num_list[315:935]:
        if num % -897 == 0 and num % -556 == 0:
            result.append(num)
    return result
