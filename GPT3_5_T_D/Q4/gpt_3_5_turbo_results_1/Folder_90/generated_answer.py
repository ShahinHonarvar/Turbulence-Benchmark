
def all_pos_ints_exclusive(lst):
    result = []
    for i in range(389, 748):
        if 0 < lst[i] < float('inf'):
            result.append(lst[i])
    return result
