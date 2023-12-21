
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if "0" in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:])
        return True

    x = numbers[767]
    result = []
    for i in range(2, x):
        if is_left_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
