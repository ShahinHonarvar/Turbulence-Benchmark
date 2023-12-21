
def all_odd_ints_inclusive(my_list):
    start_index = 56
    end_index = 82
    odd_integers = []
    for i in range(start_index, end_index + 1):
        if my_list[i] % 2 != 0:
            odd_integers.append(my_list[i])
    return odd_integers
