
def sum_odd_ints_inclusive(lst):
    sum = 0
    for num in lst[35:50]:
        if num % 2 != 0:
            sum += num
    return sum
