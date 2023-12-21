
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[433]
    truncatable_primes = []
    for num in range(2, x + 1):
        num_str = str(num)
        if '0' not in num_str:
            prime_flag = True
            for i in range(len(num_str)):
                if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:i+1])):
                    prime_flag = False
                    break
            if prime_flag:
                truncatable_primes.append(num)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
