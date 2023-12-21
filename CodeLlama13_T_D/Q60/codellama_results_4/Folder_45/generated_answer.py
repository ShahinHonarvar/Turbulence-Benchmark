
def all_left_right_truncatable_prime(numbers):
    left_truncatable = []
    right_truncatable = []
    for num in numbers:
        if is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            left_truncatable.append(num)
            right_truncatable.append(num)
    return sorted(set(left_truncatable + right_truncatable))

def is_left_truncatable_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def is_right_truncatable_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True
