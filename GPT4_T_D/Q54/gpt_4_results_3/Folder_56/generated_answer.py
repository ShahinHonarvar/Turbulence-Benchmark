
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1 or (n != 2 and n % 2 == 0):
            return False
        else:
            for number in range(3, int(n ** 0.5) + 1, 2):
                if n % number == 0:
                    return False
        return True

    def is_right_truncatable_prime(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))

    x = numbers[30]
    return sorted(filter(is_right_truncatable_prime, range(x)))
