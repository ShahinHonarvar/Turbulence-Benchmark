
def composite_nums_between_indices(lst):
    return {i for i in lst[55:99] if len({j for j in range(1, int(math.sqrt(i)) + 1) if i % j == 0}) > 2}
