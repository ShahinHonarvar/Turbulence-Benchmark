
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        num_str = str(n)
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True

    x = numbers[466]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
