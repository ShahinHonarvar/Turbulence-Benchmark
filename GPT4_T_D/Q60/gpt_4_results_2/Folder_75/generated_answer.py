
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        if "0" in str(n):
            return False
        for i in range(len(str(n))):
            if not all(is_prime(int(str(n)[i:])) and is_prime(int(str(n)[:i+1])) for i in range(len(str(n)))):
                return False
        return True

    x = numbers[41]
    return sorted([i for i in range(13, x+1) if left_right_truncatable(i)])
