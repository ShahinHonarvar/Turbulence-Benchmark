
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        for i in range(len(str_num)):
            trunc_num = int(str_num[i:])
            if not is_prime(trunc_num):
                return False
        return True

    x = numbers[89]
    result = []
    for num in range(2, x):
        if is_prime(num) and is_left_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)
