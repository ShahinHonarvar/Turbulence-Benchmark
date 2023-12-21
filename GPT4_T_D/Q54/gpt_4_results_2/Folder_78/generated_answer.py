
def all_right_truncatable_prime(numbers):
    x = numbers[23]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_right_truncatable_prime(n):
        for _ in range(len(str(n)) - 1):
            n = n // 10
            if not is_prime(n):
                return False
        return True

    result = []
    for number in range(x):
        if is_prime(number) and is_right_truncatable_prime(number):
            result.append(number)
    return sorted(result)
