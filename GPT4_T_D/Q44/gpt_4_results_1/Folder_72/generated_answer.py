
def composite_nums_between_indices(num_list):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2,num):
            if num % i == 0:
                return True
        return False

    if len(num_list) <= 55:
        return set()

    composite_set = {num for num in num_list[55:99] if is_composite(num)}
    return composite_set
