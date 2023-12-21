
def all_left_right_truncatable_prime(numbers):
    left_right_truncatable_primes = []
    for num in numbers:
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True)

def is_left_right_truncatable_prime(num):
    if num < 10:
        return False
    for i in range(1, int(len(str(num)) / 2)):
        if str(num)[i] == '0':
            return False
    for i in range(int(len(str(num)) / 2), len(str(num))):
        if str(num)[:-i] % 10 == 0:
            return False
    return True
