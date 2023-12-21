
def all_right_truncatable_prime(numbers):
    x = numbers[91]
    
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

    def is_right_truncatable(n):
        sn = str(n)
        return all(is_prime(int(sn[:i])) for i in range(1, len(sn) + 1))
                              
    return sorted([n for n in range(2, x) if is_right_truncatable(n)])
