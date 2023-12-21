
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    composites = set()
    for num in numbers[:8]:
        if not is_prime(num):
            composites.add(num)
    return composites
