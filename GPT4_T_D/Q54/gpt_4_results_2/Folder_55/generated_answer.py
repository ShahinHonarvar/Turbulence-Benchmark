
def all_right_truncatable_prime(t):
    num = t[73]
    
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for x in range(2, n):
            if n % x == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_num = str(n)
        while len(str_num) > 0:
            if is_prime(int(str_num)):
                str_num = str_num[:-1]
            else:
                return False
        return True

    result = [n for n in range(0, num) if is_right_truncatable(n)]
    return sorted(result, reverse=True)
