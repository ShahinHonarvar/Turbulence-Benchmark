
def composite_nums_between_indices(numbers):
    composites = set()
    for i in range(37, 52):
        if not is_prime(numbers[i]):
            composites.add(numbers[i])
    return composites

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
