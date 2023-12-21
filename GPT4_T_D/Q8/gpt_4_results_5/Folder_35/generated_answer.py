
def all_even_ints_exclusive(lst):
    even_ints = []
    for i in lst[11:79]:
        if i % 2 == 0:
            even_ints.append(i)
    return even_ints
