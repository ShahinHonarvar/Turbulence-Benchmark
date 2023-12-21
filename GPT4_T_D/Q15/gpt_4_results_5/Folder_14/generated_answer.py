
def sum_odd_ints_inclusive(lst):
    numbers = lst[5:8]
    total = sum([num for num in numbers if num % 2 != 0])
    return total
