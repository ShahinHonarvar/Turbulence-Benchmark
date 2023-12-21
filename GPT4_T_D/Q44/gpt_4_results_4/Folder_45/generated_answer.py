
def composite_nums_between_indices(num_list):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(40, min(201, len(num_list))):
        if is_composite(num_list[i]):
            composite_nums.add(num_list[i])
    return composite_nums
