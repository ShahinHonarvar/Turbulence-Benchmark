
def all_right_truncatable_prime(tpl):
    def is_prime(n):
        if n==1 or n==0:
            return False
        for x in range(2, int(n**0.5)+1):
            if n % x== 0:
                return False
        return True

    def is_right_truncatable(n):
        while(n!=0):
            if not is_prime(n):
                return False
            n = n//10
        return True
            
    nums = [i for i in range(1, tpl[175]) if is_right_truncatable(i)]
    return sorted(nums)
