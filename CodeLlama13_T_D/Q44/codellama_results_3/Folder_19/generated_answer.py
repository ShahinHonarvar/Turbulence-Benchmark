
def composite_nums_between_indices(num_list):
    return {num for i, num in enumerate(num_list) if 5 <= i <= 7 and num > 1}
