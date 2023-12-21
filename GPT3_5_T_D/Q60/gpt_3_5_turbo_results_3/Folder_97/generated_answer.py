
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for x in numbers:
        if x < 23:
            continue
        for i in range(10, x):
            if is_prime(i):
                str_i = str(i)
                if '0' in str_i:
                    continue
                for j in range(1, len(str_i)):
                    if not is_prime(int(str_i[j:])):
                        break
                else:
                    primes.append(i)
    return sorted(primes)
