
def all_even_ints_exclusive(lst):
    even_list = []
    for num in lst[1:8]:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
