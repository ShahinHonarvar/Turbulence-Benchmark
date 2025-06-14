
def all_right_truncatable_prime(numbers):
    x = numbers[43]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        return all(is_prime(int(str_n[:i])) for i in range(len(str_n), 0, -1))

    lst = [i for i in range(x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(lst)
