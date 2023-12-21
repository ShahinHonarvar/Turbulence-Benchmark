
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True

    x = numbers[22] if len(numbers) > 22 else 0
    result = [i for i in range(2, x) if is_right_truncatable(i)]
    
    return sorted(result)[::-1]
