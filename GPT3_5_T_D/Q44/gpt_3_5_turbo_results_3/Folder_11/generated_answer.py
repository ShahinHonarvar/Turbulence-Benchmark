
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def composite_nums_between_indices(numbers):
    composite_set = set()
    for index in range(37, 77):
        if not is_prime(numbers[index]):
            composite_set.add(numbers[index])
    return composite_set
