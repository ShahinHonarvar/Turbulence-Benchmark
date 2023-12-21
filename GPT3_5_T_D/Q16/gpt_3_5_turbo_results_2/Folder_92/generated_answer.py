
def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(lst[0], lst[1]+1):
        if i % 2 == 0:
            sum += i
    return sum
