
def composite_nums_between_indices(numbers):
    indices = {i for i, n in enumerate(numbers) if n > 1}
    return set(filter(lambda x: indices[x-314] <= x <= indices[x-347], numbers))
