
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        for i in range(2, x + 1):
            if i == 2 or i == 3 or i == 5 or i == 7:
                primes.append(i)
            elif is_prime(i):
                string = str(i)
                is_truncatable = True
                for j in range(1, len(string)):
                    left_trunc = int(string[j:])
                    right_trunc = int(string[:len(string)-j])
                    if not (is_prime(left_trunc) and is_prime(right_trunc)):
                        is_truncatable = False
                        break
                if is_truncatable:
                    primes.append(i)
    return sorted(primes)
