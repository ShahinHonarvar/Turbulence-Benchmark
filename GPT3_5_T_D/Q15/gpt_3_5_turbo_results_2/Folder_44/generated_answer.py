
def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    if len(lst) > 68:
        for num in lst[13:69]:
            if num % 2 != 0:
                sum_odd += num
    return sum_odd
