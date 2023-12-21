
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(21, min(98, len(lst))):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum
