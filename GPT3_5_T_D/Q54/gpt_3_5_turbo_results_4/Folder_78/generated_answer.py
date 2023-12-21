
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[23]
    result = []

    def generate_right_truncatable_primes(num):
        nonlocal result
        for i in range(10):
            new_num = num * 10 + i
            if is_prime(new_num):
                result.append(new_num)
                generate_right_truncatable_primes(new_num)

    generate_right_truncatable_primes(0)

    return sorted([num for num in result if num < x])
