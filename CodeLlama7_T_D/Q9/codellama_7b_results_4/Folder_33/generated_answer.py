 def all_odd_ints_inclusive(my_list):
    odd_ints = []
    for i in range(667, 774 + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
