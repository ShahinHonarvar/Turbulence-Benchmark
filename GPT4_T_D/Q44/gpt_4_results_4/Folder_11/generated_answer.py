
def composite_nums_between_indices(int_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = set()
    for i in range(37, min(77, len(int_list))):
        if is_composite(int_list[i]):
            composite_nums.add(int_list[i])
    return composite_nums
