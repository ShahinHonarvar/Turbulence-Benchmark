
def all_odd_ints_exclusive(my_list):
    odd_ints = []
    for i in range(30, 201, 2):
        if i in my_list:
            odd_ints.append(i)
    return odd_ints
