
def all_odd_ints_inclusive(my_list):
    start = 75
    end = 88
    odd_ints = []
    for i in range(start, end + 1):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
