
def all_left_right_truncatable_prime(inputs):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        if '0' in n:
            return False
        return all(is_prime(int(n[i:])) and is_prime(int(n[:len(n)-i])) for i in range(len(n)))

    limit = inputs[177]
    return sorted(i for i in range(2, limit + 1) if is_truncatable_prime(i))
