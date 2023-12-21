
def all_left_truncatable_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    x = n[79]
    result = []
    
    for i in range(2, x):
        if '0' not in str(i):
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num //= 10
            else:
                result.append(i)
    
    return sorted(result, reverse=True)
