
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[96]
    result = []
    
    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        n_str = str(n)
        while len(n_str) > 1:
            n_str = n_str[:-1]
            if not is_prime(int(n_str)):
                return False
        return True
    
    for i in range(x-1, 1, -1):
        if is_right_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result
