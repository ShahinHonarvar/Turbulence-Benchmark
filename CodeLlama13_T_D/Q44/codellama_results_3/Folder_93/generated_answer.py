
def composite_nums_between_indices(numbers):
    if len(numbers) < 23:
        return set()
    
    composites = {n for i, n in enumerate(numbers[23:]) if n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))}
    return composites
