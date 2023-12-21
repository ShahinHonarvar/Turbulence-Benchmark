
def sum_odd_ints_inclusive(lst):
    sum_val = 0
    for num in lst[14:65]:
        if num % 2 != 0:
            sum_val += num
    return sum_val
