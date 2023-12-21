
def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(667, 775):
        if i < len(int_list) and int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints
