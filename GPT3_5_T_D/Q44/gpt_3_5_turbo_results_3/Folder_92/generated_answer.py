
def composite_nums_between_indices(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    composite_nums = set()
    for num in lst[1:2]:
        if not is_prime(num):
            composite_nums.add(num)
    return composite_nums
