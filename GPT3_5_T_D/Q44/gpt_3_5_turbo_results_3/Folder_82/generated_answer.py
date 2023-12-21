
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    composite_nums = set()
    for i in range(30, 31 + 1):
        if not is_prime(lst[i]):
            composite_nums.add(lst[i])

    return composite_nums
