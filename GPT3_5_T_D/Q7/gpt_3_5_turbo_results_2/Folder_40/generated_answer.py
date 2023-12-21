
def all_even_ints_inclusive(lst):
    even_ints = []
    for i in range(min(3, len(lst))):  # only iterate up to index 2 or the length of the list, whichever is smaller
        if lst[i] % 2 == 0:
            even_ints.append(lst[i])
    return even_ints
