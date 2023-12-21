
def composite_nums_between_indices(lst):
    return {i for i in lst[68:87] if len({2, 3}) < len({d | d * i == i for d in range(1, int(i**0.5) + 1)})}
