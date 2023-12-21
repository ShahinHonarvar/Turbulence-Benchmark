
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1 or n == 0: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    
    def truncatable_prime(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i+1])): return False
        return True
    
    return sorted([x for x in numbers if truncatable_prime(x)], reverse=True)
