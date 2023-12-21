
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    return {num for index, num in enumerate(lst) if 262 <= index <= 746 and is_composite(num)}
