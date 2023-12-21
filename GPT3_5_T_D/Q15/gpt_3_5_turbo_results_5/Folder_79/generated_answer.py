
def sum_odd_ints_inclusive(lst):
    if len(lst) <= 4:
        return 0
    sum_ = 0
    for num in lst[4:5]:
        if num % 2 != 0:
            sum_ += num
    return sum_
