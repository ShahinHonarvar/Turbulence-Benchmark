
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    res = []

    for num in range(x, 1, -1):
        if '0' not in str(num):
            left_truncatable = right_truncatable = True
            while len(str(num)) >= 2 and left_truncatable:
                if not is_prime(num):
                    left_truncatable = False
                num //= 10

            num = str(num)
            while len(num) >= 2 and right_truncatable:
                if not is_prime(int(num)):
                    right_truncatable = False
                num = num[:-1]

            if left_truncatable and right_truncatable:
                res.append(num)

    return sorted(res, reverse=True)
