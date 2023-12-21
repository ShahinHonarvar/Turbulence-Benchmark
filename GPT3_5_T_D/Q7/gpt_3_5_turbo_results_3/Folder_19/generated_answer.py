
def all_even_ints_inclusive(lst):
    even_ints = []
    for index in range(3, 6):
        if index < len(lst) and lst[index] % 2 == 0:
            even_ints.append(lst[index])
    return even_ints
