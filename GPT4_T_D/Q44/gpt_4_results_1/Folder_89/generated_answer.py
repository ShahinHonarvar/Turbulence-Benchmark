
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num <= 1:
            return False
        for n in range(2, num):
            if num % n == 0:
                return True
        return False

    sublist = lst[36:47]
    composite_nums = {num for num in sublist if is_composite(num)}
    return composite_nums
