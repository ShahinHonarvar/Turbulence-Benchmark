
def sum_even_ints_inclusive(lst):
    sum_even = 0
    for idx, num in enumerate(lst):
        if 25 <= idx <= 59 and num % 2 == 0:
            sum_even += num
    return sum_even
