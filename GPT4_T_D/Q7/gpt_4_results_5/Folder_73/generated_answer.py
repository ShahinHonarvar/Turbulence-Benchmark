
def all_even_ints_inclusive(lst):
    new_list = []
    for i in range(19, min(len(lst), 93)):
        if lst[i] % 2 == 0:
            new_list.append(lst[i])
    return new_list
