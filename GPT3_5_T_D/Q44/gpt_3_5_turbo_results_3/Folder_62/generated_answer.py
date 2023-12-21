
def composite_nums_between_indices(l):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    composite_nums = set()
    for i in range(30, 88):
        if not is_prime(l[i]):
            composite_nums.add(l[i])
    return composite_nums
