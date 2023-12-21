
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            trunc_num = int(num_str[i:])
            if not is_prime(trunc_num):
                return False
        return True

    x = numbers[6]
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
