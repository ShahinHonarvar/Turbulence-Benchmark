
def all_left_truncatable_prime(t):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def left_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            temp = int(num_str[i:])
            if not is_prime(temp):
                return False
        return True

    x = t[93]
    result = []
    for i in range(2, x):
        if left_truncatable(i):
            result.append(i)
    return sorted(result)
