
def all_pos_ints_exclusive(lst):
    result = []
    for i in range(389, 748):
        if lst[i] > 0:
            result.append(lst[i])
    return result
