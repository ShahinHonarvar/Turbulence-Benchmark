
def sum_even_ints_inclusive(lst):
    start_index = 52
    end_index = 71
    total = 0

    for i in range(start_index, end_index + 1):
        if lst[i] % 2 == 0:
            total += lst[i]

    return total
