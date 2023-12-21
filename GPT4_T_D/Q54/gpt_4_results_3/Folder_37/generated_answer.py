
def all_right_truncatable_prime(tup):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable(n):
        num = str(n)
        for i in range(len(num)):
            if not is_prime(int(num[i:])):
                return False
        return True

    x = tup[35]
    result = [i for i in range(2, x) if is_prime(i) and is_right_truncatable(i)]
    return sorted(result, reverse=True)
