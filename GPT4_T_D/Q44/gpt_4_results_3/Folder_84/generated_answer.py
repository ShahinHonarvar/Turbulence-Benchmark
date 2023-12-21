
def composite_nums_between_indices(int_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return {num for i, num in enumerate(int_list[30:49]) if is_composite(num)}
