
def all_right_truncatable_prime(input_tuple):
    x = input_tuple[645]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        return all(is_prime(int(n[i:])) for i in range(len(n)))

    result = []
    for i in range(x):
        if is_prime(i) and is_truncatable_prime(i):
            result.append(i)

    return sorted(result)
