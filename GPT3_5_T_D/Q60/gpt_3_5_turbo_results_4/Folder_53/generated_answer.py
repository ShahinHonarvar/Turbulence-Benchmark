
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def all_left_right_truncatable_prime(numbers):
    x = numbers[86]
    result = []

    for num in range(x, 10, -1):
        num_str = str(num)
        if '0' in num_str:
            continue
        truncatable_prime = True

        for i in range(len(num_str)):
            left_truncated = int(num_str[:i+1])
            right_truncated = int(num_str[i:])

            if not is_prime(left_truncated) or not is_prime(right_truncated):
                truncatable_prime = False
                break

        if truncatable_prime:
            result.append(num)

    return sorted(result, reverse=True)
