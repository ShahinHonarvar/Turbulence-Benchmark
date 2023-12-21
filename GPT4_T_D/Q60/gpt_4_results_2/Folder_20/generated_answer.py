
def all_left_right_truncatable_prime(tup):
    x = tup[100]
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n, m):
        return all(is_prime(int(str(n)[i:m])) for i in range(m))

    result = [i for i in range(11, x+1) if str(i).find('0') == -1 and is_truncatable(i, len(str(i)))
              and is_truncatable(i, -len(str(i)))]
    return sorted(result, reverse=True)
