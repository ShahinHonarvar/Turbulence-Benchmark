
def sum_even_ints_inclusive(lst):
    total = 0
    for i in range(75, 89):
        if i < len(lst) and lst[i] % 2 == 0:
            total += lst[i]
    return total
