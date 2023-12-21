
def all_ints_div_by_both_two_nums(lst):
    divisors = [-897, -556]
    result = []
    for i in range(315, 935):
        if all(lst[i] % d == 0 for d in divisors):
            result.append(lst[i])
    return result
