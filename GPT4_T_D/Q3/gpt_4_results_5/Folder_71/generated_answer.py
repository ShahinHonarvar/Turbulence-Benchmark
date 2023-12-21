
def all_pos_ints_inclusive(lst):
    postive_ints = []
    for i in range(26, 53):
        if lst[i] > 0:
            postive_ints.append(lst[i])
    return postive_ints
