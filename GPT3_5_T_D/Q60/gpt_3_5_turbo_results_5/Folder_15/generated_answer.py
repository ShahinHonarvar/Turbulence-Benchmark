
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        else:
            return is_prime(n) and is_truncatable_prime(int(str(n)[1:-1]))

    x = numbers[6]
    result = []
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result
