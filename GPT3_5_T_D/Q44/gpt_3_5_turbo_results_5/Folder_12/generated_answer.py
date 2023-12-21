
def composite_nums_between_indices(lst):
    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(51, 87):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])

    return composite_nums
