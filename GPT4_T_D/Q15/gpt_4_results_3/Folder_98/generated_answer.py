
def sum_odd_ints_inclusive(lst):
    summed = sum([num for index, num in enumerate(lst[:7]) if num % 2 != 0])
    return summed
