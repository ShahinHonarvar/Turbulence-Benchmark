
def composite_nums_between_indices(num_list):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return True
        return False
    
    composite_nums = {num for num in num_list[51:87] if is_composite(num)}
    return composite_nums
