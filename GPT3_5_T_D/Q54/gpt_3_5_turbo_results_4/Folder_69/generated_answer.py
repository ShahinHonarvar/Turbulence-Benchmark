
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[760]
    right_truncatable_primes = []
    for num in range(x, 10, -1):
        if is_prime(num):
            num_str = str(num)
            while len(num_str) > 1:
                num_str = num_str[:-1]
                if not is_prime(int(num_str)):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)
