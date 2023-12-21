
def composite_nums_between_indices(list):
    indices = range(667, 775)
    return { num for i, num in enumerate(list) if i in indices and not is_prime(num) }
