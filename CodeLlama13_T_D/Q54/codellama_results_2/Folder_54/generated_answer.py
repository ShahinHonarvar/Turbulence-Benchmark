
def all_right_truncatable_prime(numbers):
    x = numbers[88]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_str = str(i)
            while len(prime_str) > 0:
                prime_num = int(prime_str[::-1])
                if not is_prime(prime_num):
                    break
                primes.append(prime_num)
                prime_str = prime_str[:-1]
    return sorted(primes, reverse=True)
