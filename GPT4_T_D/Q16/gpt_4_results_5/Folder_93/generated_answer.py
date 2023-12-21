
def sum_even_ints_inclusive(lst):
    sum = 0
    for i in lst[75:95]:
        if i % 2 == 0:
            sum += i
    return sum
