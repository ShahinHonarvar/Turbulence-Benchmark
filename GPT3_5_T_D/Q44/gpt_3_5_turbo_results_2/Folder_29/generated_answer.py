
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    composite_nums = {num for num in lst[52:72] if is_composite(num)}
    return composite_nums
