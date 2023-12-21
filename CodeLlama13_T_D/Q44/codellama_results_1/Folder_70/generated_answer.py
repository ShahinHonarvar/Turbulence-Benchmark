
def composite_nums_between_indices(numbers):
    indices = [32, 35]
    return {number for i, number in enumerate(numbers) if i >= indices[0] and i <= indices[1] and not is_prime(number)}
