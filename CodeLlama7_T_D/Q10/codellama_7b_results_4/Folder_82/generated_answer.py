
def all_odd_ints_exclusive(my_list):
    odd_ints = []
    for i in range(20, 201):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
