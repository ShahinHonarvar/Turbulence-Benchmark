
def all_left_right_truncatable_prime(numbers):
    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(1, len(str(n))):
            if not check_prime(int(str(n)[i:])) or not check_prime(int(str(n)[:-i])):
                return False
        return True

    x = numbers[77]
    truncatables = []
    for i in range(2, x + 1):
        if check_prime(i) and check_truncatable(i):
            truncatables.append(i)
    return sorted(truncatables, reverse=True)
