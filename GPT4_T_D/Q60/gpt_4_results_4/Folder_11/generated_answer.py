
def all_left_right_truncatable_prime(t):
    from sympy import isprime
    def check_prime(num):
        return all(isprime(int(num[i:])) and isprime(int(num[:len(num)-i])) for i in range(len(num)))

    x = t[86]
    prime_numbers = ['2', '3', '5', '7']
    for num in range(23, x + 1, 2):
        if '0' not in str(num) and check_prime(str(num)):
            prime_numbers.append(str(num))
    return list(map(int, prime_numbers))
