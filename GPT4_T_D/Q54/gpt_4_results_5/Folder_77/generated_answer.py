
def all_right_truncatable_prime(tup):
    x = tup[767]
    def truncatable_prime(n):
        str_num = str(n)
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for num in range(2, x):
        if truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result
