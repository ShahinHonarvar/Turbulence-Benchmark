
def all_odd_ints_exclusive(my_list):
    start = 62
    end = 96
    odd_ints = []
    for i in range(start, end):
        if my_list[i] % 2 != 0:
            odd_ints.append(my_list[i])
    return odd_ints
