
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for index in range(23, 24):
        if index < len(num_list) and is_composite(num_list[index]):
            composite_nums.add(num_list[index])
    return composite_nums
