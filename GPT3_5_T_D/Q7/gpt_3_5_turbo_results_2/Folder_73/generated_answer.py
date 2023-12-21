
def all_even_ints_inclusive(lst):
    even_ints = []
    for num in lst[19:93]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints
