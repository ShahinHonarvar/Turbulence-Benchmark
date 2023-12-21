
def sum_even_ints_inclusive(lst):
    even_ints = []
    for i in range(3):
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return sum(even_ints)
