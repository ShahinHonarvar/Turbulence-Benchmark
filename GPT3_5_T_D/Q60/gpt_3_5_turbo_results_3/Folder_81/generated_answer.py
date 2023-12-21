
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        string_num = str(num)
        while len(string_num) > 1:
            string_num = string_num[1:]
            if not is_prime(int(string_num)):
                return False
        return True

    def is_right_truncatable(num):
        string_num = str(num)
        while len(string_num) > 1:
            string_num = string_num[:-1]
            if not is_prime(int(string_num)):
                return False
        return True

    x = numbers[98]
    results = []

    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_left_truncatable(num) and is_right_truncatable(num):
            results.append(num)

    return sorted(results)
