
def all_even_ints_exclusive(lst):
    even = []
    for i in range(62, 96):
        if lst[i]%2 == 0:
            even.append(lst[i])
    return even
