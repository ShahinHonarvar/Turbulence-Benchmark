
def all_left_right_truncatable_prime(numbers):
    result = []
    for num in numbers:
        if is_left_and_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)

def is_left_and_right_truncatable_prime(num):
    if num < 10 or num % 11 != 0:
        return False
    for i in range(1, int(len(str(num)) / 2)):
        if num % 10**i != 0 and not is_left_right_truncatable_prime(num, i):
            return False
    return True

def is_left_right_truncatable_prime(num, k):
    left = int(str(num)[:-k])
    right = int(str(num)[k:])
    if left % 10**(len(str(num)) - k) != 0 or right % 10**k != 0:
        return False
    for i in range(1, k):
        if not is_left_right_truncatable_prime(left, i) or not is_left_right_truncatable_prime(right, i):
            return False
    return True
