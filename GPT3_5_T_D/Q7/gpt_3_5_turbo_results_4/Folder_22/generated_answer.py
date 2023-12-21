
def all_even_ints_inclusive(lst):
    evens = []
    for num in lst[40:201]:
        if num % 2 == 0:
            evens.append(num)
    return evens
