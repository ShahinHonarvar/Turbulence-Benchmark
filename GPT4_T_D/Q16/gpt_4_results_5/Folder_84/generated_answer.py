
def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(max(0, 43), min(87, len(lst))):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum
