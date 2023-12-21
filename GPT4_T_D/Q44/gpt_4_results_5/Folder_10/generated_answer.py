
def composite_nums_between_indices(lst):
    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return True
        return False

    output_set = set()
    for i in range(37, min(52, len(lst))):
        if is_composite(lst[i]):
            output_set.add(lst[i])
    return output_set
