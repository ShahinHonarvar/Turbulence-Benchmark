
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(numbers):
    composite_nums = set()
    for index in range(80, 201):
        if is_prime(numbers[index]):
            composite_nums.add(numbers[index])
    return composite_nums
