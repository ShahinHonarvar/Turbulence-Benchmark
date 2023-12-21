
def all_left_right_truncatable_prime(nums):
    x = nums[67]
    primes = []
    
    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

    def left_right_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not (is_prime(int(str(n)[i:])) and is_prime(int(str(n)[:len(str(n))-i]))):
                return False
        return True

    for num in range(2, x + 1):
        if is_prime(num) and left_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)
