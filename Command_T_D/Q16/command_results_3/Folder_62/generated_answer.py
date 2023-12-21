def sum_even_ints_inclusive(lst):
    even_ints = [i for i in range(92, 100, 2) if lst[i] % 2 == 0]
    return sum(lst[even_ints[0]:even_ints[-1] + 1]) if even_ints else 0
