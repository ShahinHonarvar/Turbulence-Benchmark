
def all_ints_div_by_both_two_nums(nums):
    result = []
    for n in range(10, 101):
        if n % 10 == 0 and n % 100 == 0:
            result.append(n)
    return result
