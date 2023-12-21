
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for index in range(34, min(56, len(num_list))):
        if is_composite(num_list[index]):
            composite_nums.add(num_list[index])
    return composite_nums
