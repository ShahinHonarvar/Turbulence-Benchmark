
def all_ints_div_by_both_two_nums(lst):
    results = []
    for i in range(70, 201):
        if lst[i] % 3 == 0 and lst[i] % -300 == 0:
            results.append(lst[i])
    return results
