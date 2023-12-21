
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return set([num for i, num in enumerate(num_list[56:67]) if is_composite(num)])
