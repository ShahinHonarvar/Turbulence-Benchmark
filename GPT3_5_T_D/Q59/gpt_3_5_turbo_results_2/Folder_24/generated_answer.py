
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[65]
    left_truncatable_primes = []
    
    for num in range(x-1, 1, -1):
        if '0' in str(num):
            continue
        truncatable = True
        num_str = str(num)
        while num_str:
            if not is_prime(int(num_str)):
                truncatable = False
                break
            num_str = num_str[1:]
        if truncatable:
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes, reverse=True)
