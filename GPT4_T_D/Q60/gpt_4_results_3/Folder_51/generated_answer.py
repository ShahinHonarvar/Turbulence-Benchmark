
def all_left_right_truncatable_prime(tup):
    def is_prime(n):
        if n in (2,3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def left_right_trunc(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not(is_prime(int(str_n[i:])) and is_prime(int(str_n[:len(str_n)-i]))):
                return False
        return True

    x = tup[54]
    result = []
    for i in range(10, x + 1):
        if '0' in str(i):
            continue
        if is_prime(i) and left_right_trunc(i):
            result.append(i)
    return sorted(result)
