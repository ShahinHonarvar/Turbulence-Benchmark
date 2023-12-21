
def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for num in lst[26:53]:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd
