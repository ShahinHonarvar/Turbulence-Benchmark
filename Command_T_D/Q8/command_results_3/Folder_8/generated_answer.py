def all_even_ints_exclusive(lst):
    evens = []
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            evens.append(lst[i])
            if len(evens) == 7:
                break
    return evens
