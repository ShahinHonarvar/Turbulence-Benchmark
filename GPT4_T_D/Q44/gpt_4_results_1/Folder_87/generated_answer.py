
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    comp_nums = {i for i in num_list[43:52] if is_composite(i)}
    return comp_nums
