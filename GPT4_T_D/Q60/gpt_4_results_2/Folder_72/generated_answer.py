
def all_left_right_truncatable_prime(nums):
    from sympy import isprime
    
    def check_prime(n):
        n = str(n)
        if '0' in n:
            return False
        for i in range(len(n)):
            if not isprime(int(n[i:])) or not isprime(int(n[:len(n)-i])):
                return False
        return True

    x = nums[31]
    result = [i for i in range(10, x+1) if check_prime(i)]
    result.sort(reverse=True)
    return result
