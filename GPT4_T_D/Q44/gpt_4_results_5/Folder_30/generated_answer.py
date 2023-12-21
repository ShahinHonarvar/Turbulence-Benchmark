
def composite_nums_between_indices(num_list):
    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    return set([num for num in num_list[19:93] if is_composite(num)])
