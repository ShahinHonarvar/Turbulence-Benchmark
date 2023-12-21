
def all_right_truncatable_prime(t):
    x = t[0]
    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    def is_right_truncatable(n):
        for i in range(len(str(n))): 
            if not is_prime(n):
                return False
            n = n // 10
        return True
    result = [i for i in range(2, x) if is_right_truncatable(i)]
    result.sort(reverse=True)
    return result
