
def all_left_right_truncatable_prime(numbers):
    x = numbers[91]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
            if not is_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    return sorted(filter(lambda n: is_prime(n) and is_truncatable(n), range(x+1)))
