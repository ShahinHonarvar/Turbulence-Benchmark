
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    truncatable_primes = []
    for x in numbers:
        if x < 10:  # Single-digit numbers are not truncatable primes
            continue
        str_x = str(x)
        if '0' in str_x:  # Truncatable primes should not contain 0
            continue
        
        is_truncatable_prime = True
        for i in range(1, len(str_x)):
            left_truncated = int(str_x[i:])
            right_truncated = int(str_x[:i])

            if not is_prime(left_truncated) or not is_prime(right_truncated):
                is_truncatable_prime = False
                break

        if is_truncatable_prime:
            truncatable_primes.append(x)
    
    return sorted(truncatable_primes)
