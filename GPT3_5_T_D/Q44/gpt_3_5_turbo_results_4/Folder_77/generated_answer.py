
def composite_nums_between_indices(lst):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    composite_nums = set()
    for num in lst[667:775]:
        if not is_prime(num):
            composite_nums.add(num)
    return composite_nums
