
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[61]
    result = []
    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            n = num
            while n > 0:
                if not is_prime(n):
                    right_truncatable = False
                    break
                n //= 10
            if right_truncatable:
                result.append(num)
    return sorted(result)
