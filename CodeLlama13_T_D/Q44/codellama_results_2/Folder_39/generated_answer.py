
def composite_nums_between_indices(arr):
    return set(filter(lambda x: x > 62 and x < 93 and x % 2 != 0, arr))
