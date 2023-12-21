
def all_ints_div_by_both_two_nums(lst):
    results = []
    for i in range(138, 425):
        if lst[i] % -863 == 0 and lst[i] % -329 == 0:
            results.append(lst[i])
    return results
