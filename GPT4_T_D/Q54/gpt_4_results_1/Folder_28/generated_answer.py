
def all_right_truncatable_prime(value_tuple):
    def is_prime(n):
        if n == 1:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    def right_truncatable(n):
        for c in range(len(str(n))):
            if not is_prime(int(str(n)[:len(str(n))-c])):
                return False
        return True

    x = value_tuple[19]
    prime_list = []

    for num in range(1, x):
        if right_truncatable(num):
            prime_list.append(num)

    return sorted(prime_list)
