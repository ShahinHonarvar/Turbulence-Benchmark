
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    output = set([num for num in num_list[91:100] if is_composite(num)])
    return output
