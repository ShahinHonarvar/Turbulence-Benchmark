
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(len(lst)):
        if i >= 0 and i <= 6 and lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
