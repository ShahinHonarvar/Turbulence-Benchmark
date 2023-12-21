
def sum_even_ints_inclusive(lst):
    sum = 0
    for num in lst[8:81]:
        if num % 2 == 0:
            sum += num
    return sum
