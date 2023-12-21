
def composite_nums_between_indices(num_list):
    return {num for i, num in enumerate(num_list) if 28 <= i <= 32 and not is_prime(num)}
