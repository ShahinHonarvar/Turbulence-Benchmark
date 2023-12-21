
def all_odd_ints_inclusive(my_list):
    odd_integers = []
    for i in range(1, 6):
        if my_list[i] % 2 == 1:
            odd_integers.append(my_list[i])
    return odd_integers
