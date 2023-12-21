
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    x = numbers[65]
    primes = []
    for number in range(x, 1, -1):
        if is_prime(number) and '0' not in str(number):
            str_number = str(number)
            for i in range(1, len(str_number)):
                left_truncated = int(str_number[i:])
                right_truncated = int(str_number[:i])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    break
            else:
                primes.append(number)
    return primes
