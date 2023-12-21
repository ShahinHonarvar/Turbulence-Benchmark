
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(70, 201):
        if i % 2 == 0 and i < len(lst):
            even_sum += lst[i]
    return even_sum
