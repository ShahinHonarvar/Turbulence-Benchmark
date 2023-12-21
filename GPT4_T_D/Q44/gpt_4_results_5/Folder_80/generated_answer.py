
def composite_nums_between_indices(lst):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    nums = lst[62:79]
    composite_nums = {num for num in nums if is_composite(num)}
    return composite_nums
