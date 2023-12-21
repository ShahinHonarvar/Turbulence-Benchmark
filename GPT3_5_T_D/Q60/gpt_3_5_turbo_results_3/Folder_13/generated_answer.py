
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    valid_primes = []
    for x in numbers:
        if is_prime(x):
            s = str(x)
            if '0' not in s:
                valid = True
                for i in range(len(s)):
                    if not is_prime(int(s[i:])) or not is_prime(int(s[:i+1])):
                        valid = False
                        break
                if valid:
                    valid_primes.append(x)
    return sorted(valid_primes)
