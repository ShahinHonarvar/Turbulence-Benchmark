
def sum_even_ints_inclusive(lst):
    sum = 0
    for num in lst[33:37]:
        if num % 2 == 0:
            sum += num
    return sum
