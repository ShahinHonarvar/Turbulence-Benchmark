
def sum_even_ints_inclusive(lst):
    result = 0
    for num in lst[19:93]:
        if num % 2 == 0:
            result += num
    return result
