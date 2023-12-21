
def all_left_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(n):
    if n < 2 or (n % 2 == 0 and n != 2):
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
