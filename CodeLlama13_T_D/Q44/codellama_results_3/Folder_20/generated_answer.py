
def composite_nums_between_indices(numbers):
    indices = range(74, 96)
    return {number for i, number in enumerate(numbers) if i in indices and not is_prime(number)}

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
