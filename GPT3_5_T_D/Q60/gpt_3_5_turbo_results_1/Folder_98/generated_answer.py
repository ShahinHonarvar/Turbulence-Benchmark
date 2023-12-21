
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str) + 1):
            if not is_prime(int(num_str[:i])) or not is_prime(int(num_str[-i:])):
                return False
        return True

    x = numbers[8]
    results = []

    for num in range(2, x+1):
        if is_truncatable_prime(num):
            results.append(num)

    return sorted(results, reverse=True)
