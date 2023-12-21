
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = [num for num in num_list[30:31] if is_composite(num)]
    return set(composite_nums)
