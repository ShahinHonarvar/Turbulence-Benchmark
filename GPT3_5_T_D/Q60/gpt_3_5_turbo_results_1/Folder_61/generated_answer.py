
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[3]
    primes = []
    for number in range(2, x + 1):
        if is_prime(number):
            number_str = str(number)
            if '0' not in number_str:
                all_prime = True
                for i in range(1, len(number_str)):
                    left_truncated = int(number_str[i:])
                    right_truncated = int(number_str[:i])
                    if not is_prime(left_truncated) or not is_prime(right_truncated):
                        all_prime = False
                        break
                if all_prime:
                    primes.append(number)
    return sorted(primes, reverse=True)
