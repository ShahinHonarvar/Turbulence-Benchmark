
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    x = numbers[96]
    for n in range(2, x + 1):
        if is_prime(n):
            string_n = str(n)
            if '0' in string_n:
                continue
            left_truncatable = True
            right_truncatable = True
            for i in range(1, len(string_n)):
                if not is_prime(int(string_n[i:])):
                    right_truncatable = False
                    break
            for i in range(len(string_n) - 1, 0, -1):
                if not is_prime(int(string_n[:i])):
                    left_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(n)
    
    primes.sort(reverse=True)
    return primes
