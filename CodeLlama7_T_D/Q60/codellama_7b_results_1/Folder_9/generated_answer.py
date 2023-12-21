 def all_left_right_truncatable_prime(tuple):
    x = tuple[29]
    left_right_truncatable_prime_numbers = []
    for i in range(1, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            left_right_truncatable_prime_numbers.append(i)
    return sorted(left_right_truncatable_prime_numbers, reverse=True)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    string = str(n)
    length = len(string)

    for i in range(length - 1):
        if not string[i].isdigit():
            return False

        if not string[length - 2 - i].isdigit():
            return False

    return True
