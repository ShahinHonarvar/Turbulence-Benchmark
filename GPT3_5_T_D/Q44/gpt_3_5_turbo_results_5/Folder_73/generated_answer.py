
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(28, 41):
        if not is_prime(numbers[i]):
            composites.add(numbers[i])
    return composites
