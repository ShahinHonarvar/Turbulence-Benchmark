
def all_even_ints_inclusive(lst):
    even_lst = []
    for i in range(60, 201):
        if i % 2 == 0:
            even_lst.append(lst[i])
    return even_lst
