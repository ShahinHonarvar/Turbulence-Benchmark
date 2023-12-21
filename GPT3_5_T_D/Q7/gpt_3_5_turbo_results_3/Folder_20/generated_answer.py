
def all_even_ints_inclusive(lst):
    even_nums = []
    for i in range(56, 67):
        if lst[i] % 2 == 0:
            even_nums.append(lst[i])
    return even_nums
