
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for x in numbers:
        if x <= 23:
            continue
        str_x = str(x)
        if '0' in str_x:
            continue
        left_truncatable = True
        right_truncatable = True
        for i in range(len(str_x)):
            if not is_prime(int(str_x[i:])):
                right_truncatable = False
                break
            if not is_prime(int(str_x[:i+1])):
                left_truncatable = False
                break
        if left_truncatable and right_truncatable:
            result.append(x)

    return sorted(result)
