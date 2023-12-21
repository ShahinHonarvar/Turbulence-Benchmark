
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_composite(n):
        return not is_prime(n)

    composite_nums = set()
    for i in range(74, 96):
        if is_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums
