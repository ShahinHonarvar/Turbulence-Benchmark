
def all_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_str = str(i)
            for j in range(len(prime_str)):
                if not is_prime(int(prime_str[:-j])):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)
