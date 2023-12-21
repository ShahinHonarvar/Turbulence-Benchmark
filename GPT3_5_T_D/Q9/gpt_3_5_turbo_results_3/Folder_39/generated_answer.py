
def all_odd_ints_inclusive(integer_list):
    odd_ints = []
    for i in range(20, 31):
        if integer_list[i] % 2 != 0:
            odd_ints.append(integer_list[i])
    return odd_ints
