
def sum_even_ints_inclusive(int_list):
    sublist = int_list[533:606]
    even_list = [i for i in sublist if i % 2 == 0]
    if even_list != []:
        return sum(even_list)
    else:
        return 0
