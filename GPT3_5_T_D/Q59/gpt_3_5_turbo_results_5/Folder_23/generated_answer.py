
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    primes = []
    for i in range(10, x):
        if '0' not in str(i):
            temp_i = str(i)
            is_left_truncatable_prime = True
            while temp_i:
                if not is_prime(int(temp_i)):
                    is_left_truncatable_prime = False
                    break
                temp_i = temp_i[1:]
            if is_left_truncatable_prime:
                primes.append(i)
    return sorted(primes, reverse=True)
