
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    composite_set = set()
    for i in range(75, 86):
        if not is_prime(numbers[i]):
            composite_set.add(numbers[i])
    return composite_set
