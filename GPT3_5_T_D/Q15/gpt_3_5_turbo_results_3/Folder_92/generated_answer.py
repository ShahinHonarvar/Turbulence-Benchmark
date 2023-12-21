
def sum_odd_ints_inclusive(lst):
    sum = 0
    for num in lst[1:1]:
        if num % 2 != 0:
            sum += num
    return sum
