
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[992]
    result = []
    for i in range(2, x):
        if is_prime(i):
            truncatable = True
            number = str(i)
            while truncatable and number:
                if not is_prime(int(number)):
                    truncatable = False
                number = number[:-1]
            if truncatable:
                result.append(i)
    return sorted(result)
