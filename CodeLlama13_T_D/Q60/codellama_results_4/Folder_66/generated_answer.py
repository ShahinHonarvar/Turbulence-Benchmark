
def all_left_right_truncatable_prime(numbers):
    return sorted([num for num in range(*numbers) if is_left_and_right_truncatable_prime(num)], reverse=True)

def is_left_and_right_truncatable_prime(n):
    if n < 10 or str(n).count("0") > 0:
        return False
    for i in range(len(str(n)) - 1):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i + 1:])):
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
