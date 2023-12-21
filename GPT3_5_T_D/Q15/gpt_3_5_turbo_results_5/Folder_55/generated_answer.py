
def sum_odd_ints_inclusive(lst):
    sum = 0
    for num in lst[:11]:
        if num % 2 == 1:
            sum += num
    return sum
