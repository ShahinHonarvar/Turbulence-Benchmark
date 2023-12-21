
def all_left_right_truncatable_prime(numbers):
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_prime(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not check_prime(int(str(n)[i:])) or not check_prime(int(str(n)[:len(str(n)) - i])):
                return False
        return True

    x = numbers[93]
    return sorted(filter(truncatable_prime, range(10, x+1)))
