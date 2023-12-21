
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and i not in [2, 3, 5, 7]:
            str_i = str(i)
            if '0' in str_i:
                continue
            is_left_right_truncatable_prime = True
            for j in range(len(str_i)):
                trunc_i = int(str_i[j:])
                if not is_prime(trunc_i):
                    is_left_right_truncatable_prime = False
                    break
            if is_left_right_truncatable_prime:
                primes.append(i)
    return sorted(primes, reverse=True)
