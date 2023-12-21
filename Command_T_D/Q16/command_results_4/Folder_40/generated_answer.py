def sum_even_ints_inclusive(lst):
    even_ints = [y for y in range(len(lst)) if lst[y] % 2 == 0]
    if even_ints:
        return sum(lst[even_ints[0]:even_ints[1] + 1])
    else:
        return 0
