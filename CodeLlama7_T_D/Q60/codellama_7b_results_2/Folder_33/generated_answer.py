
def all_left_right_truncatable_prime(tuple):
    x = tuple[945]
    list = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            list.append(i)
    return sorted(list, reverse=True)
def is_left_right_truncatable_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    digits = [int(digit) for digit in str(n)]
    for i in range(len(digits)):
        if digits[i] == 0:
            return False

        if digits[i] != digits[-i - 1]:
            return False

    return True
