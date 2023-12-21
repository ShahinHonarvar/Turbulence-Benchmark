
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i== 0:
                return False
        return True

    def is_right_truncatable(num):
        if int(num) < 10:
            return is_prime(int(num))
        return is_prime(int(num)) and is_right_truncatable(num[:-1])

    x = numbers[70]
    right_truncatable_primes = []

    for i in range(2, x):
        if is_right_truncatable(str(i)):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes)
