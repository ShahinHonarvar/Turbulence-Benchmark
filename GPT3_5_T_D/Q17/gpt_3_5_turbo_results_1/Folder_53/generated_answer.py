
def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[200:201]:
        if num % 17 == 0 and num % -5 == 0:
            result.append(num)
    return result
