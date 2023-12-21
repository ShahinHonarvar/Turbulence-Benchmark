
def all_right_truncatable_prime(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = lst[803]
    result = []

    for num in range(10, x):
        if is_prime(num):
            truncatable = True
            digits = str(num)
            for i in range(1, len(digits)):
                if not is_prime(int(digits[:-i])):
                    truncatable = False
                    break
            if truncatable:
                result.append(num)

    return sorted(result)
