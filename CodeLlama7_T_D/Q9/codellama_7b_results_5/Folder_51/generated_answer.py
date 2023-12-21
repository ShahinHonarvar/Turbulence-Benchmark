
def all_odd_ints_inclusive(my_list):
    odd_ints = []
    for i in range(1, len(my_list) + 1):
        if my_list[i - 1] % 2 != 0:
            odd_ints.append(my_list[i - 1])
    return odd_ints
