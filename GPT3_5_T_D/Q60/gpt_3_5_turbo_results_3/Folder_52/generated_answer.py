
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if "0" in str(n):
            return False
        while len(str(n)) > 2:
            if not is_prime(int(str(n)[1:-1])):
                return False
            n = int(str(n)[:-1])
        return True

    x = numbers[52]
    results = []
    for i in range(x, 1, -1):
        if is_prime(i) and is_truncatable_prime(i):
            results.append(i)

    return sorted(results, reverse=True)
