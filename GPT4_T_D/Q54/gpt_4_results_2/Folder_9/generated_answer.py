
def all_right_truncatable_prime(t):
    x = t[29]
    def is_prime(n):
        if n==1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def right_truncatable(num):
        while num > 0:
            if not is_prime(num):
                return False
            num = num // 10
        return True

    result = []
    for i in range(2,x):
        if right_truncatable(i):
            result.append(i)
    return sorted(result, reverse=True)
