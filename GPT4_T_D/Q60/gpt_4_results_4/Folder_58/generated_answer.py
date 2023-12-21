
def all_left_right_truncatable_prime(tup):
    x = tup[975]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True

    lst = [i for i in range(10, x + 1) if is_prime(i) and check_truncatable(i)]
    lst.sort(reverse=True)

    return lst
