
def all_right_truncatable_prime(tuple_of_numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tuple_of_numbers[84]
    result = [num for num in range(2, x) if is_right_truncatable_prime(num)]
    result.sort(reverse=True)
    return result
