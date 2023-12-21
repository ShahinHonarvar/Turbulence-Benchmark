
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[100]
    results = []

    def check_right_truncatable_prime(n):
        if is_prime(n):
            if len(str(n)) == 1:
                results.append(n)
            else:
                check_right_truncatable_prime(int(str(n)[:-1]))

    for num in range(x-1, 1, -1):
        check_right_truncatable_prime(num)

    return sorted(results, reverse=True)
