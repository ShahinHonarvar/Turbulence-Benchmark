
def sum_even_ints_inclusive(lst):
    integers = lst[3:6]
    sum = 0
    for num in integers:
        if num % 2 == 0:
            sum += num
    return sum
