
def all_left_right_truncatable_prime(int_tuple):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable(num):
        str_n = str(num)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    x = int_tuple[36]
    res = [i for i in range(11, x + 1) if truncatable(i)]
    return sorted(res, reverse=True)
