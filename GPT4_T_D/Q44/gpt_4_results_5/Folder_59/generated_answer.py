
def composite_nums_between_indices(numbers):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for index, num in enumerate(numbers[:10]):
        if is_composite(num):
            composite_nums.add(num)

    return composite_nums
