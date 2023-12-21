
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[19]
    results = []

    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_right_truncatable = True

            for i in range(1, len(num_str)):
                if not is_prime(int(num_str[:-i])):
                    is_right_truncatable = False
                    break

            if is_right_truncatable:
                results.append(num)

    return sorted(results)
