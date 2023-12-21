
def composite_nums_between_indices(num_list):
    def check_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(21, 98):
        if i < len(num_list) and check_composite(num_list[i]):
            composite_nums.add(num_list[i])

    return composite_nums
