
def all_even_ints_inclusive(lst):
    output = []
    for i in range(533, 606):
        if lst[i] % 2 == 0:
            output.append(lst[i])
    return output
