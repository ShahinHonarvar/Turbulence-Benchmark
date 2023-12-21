
def all_even_ints_inclusive(lst):
    even_lst = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
        if len(even_lst) == 7:
            break
    return even_lst[:7]
