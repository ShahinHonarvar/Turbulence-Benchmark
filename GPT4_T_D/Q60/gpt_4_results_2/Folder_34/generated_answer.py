
def all_left_right_truncatable_prime(nums):
    x = nums[18]

    def is_prime(n):
        if n==1 or n==0:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:len(str_num)-i])):
                return False
        return True

    truncatable_primes = [i for i in range(x+1) if is_left_right_truncatable(i)]
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
