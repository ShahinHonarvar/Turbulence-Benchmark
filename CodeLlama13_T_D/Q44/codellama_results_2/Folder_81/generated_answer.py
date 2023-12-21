
def composite_nums_between_indices(my_list):
    return {num for i, num in enumerate(my_list) if 20 <= i <= 200 and not is_prime(num)}
