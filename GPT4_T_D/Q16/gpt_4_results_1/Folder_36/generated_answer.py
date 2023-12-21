
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(246, 751):
        try:
            if lst[i] % 2 == 0:
                even_sum += lst[i]
        except IndexError:
            break
    return even_sum
