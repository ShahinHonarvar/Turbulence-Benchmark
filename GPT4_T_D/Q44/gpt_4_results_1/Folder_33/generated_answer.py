
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2: 
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_nums = {num for idx, num in enumerate(num_list) if 314 <= idx <= 347 and is_composite(num)}
    return composite_nums
