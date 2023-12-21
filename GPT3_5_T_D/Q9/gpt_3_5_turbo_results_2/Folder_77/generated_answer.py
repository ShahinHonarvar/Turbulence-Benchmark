
def all_odd_ints_inclusive(integer_list):
    odd_ints = []
    for i in range(527, 539):
        if i < len(integer_list) and integer_list[i] % 2 != 0:
            odd_ints.append(integer_list[i])
    return odd_ints
