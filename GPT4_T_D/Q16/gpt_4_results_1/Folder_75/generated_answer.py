
def sum_even_ints_inclusive(lst):
    slice = lst[56:58]
    sum = 0
    for num in slice:
        if num % 2 == 0:
            sum += num
    return sum
