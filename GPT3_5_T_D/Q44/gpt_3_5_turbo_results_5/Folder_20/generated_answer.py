
def composite_nums_between_indices(nums_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    composite_nums = set()
    for i in range(74, 96):
        if not is_prime(nums_list[i]):
            composite_nums.add(nums_list[i])

    return composite_nums
