
def sum_odd_ints_inclusive(lst):
    result = 0
    for num in lst[34:56]:
        if num % 2 == 1:
            result += num
    return result
