
def all_right_truncatable_prime(nums):
    x = nums[97]
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True

    def right_truncatable_primes(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
        return True

    right_truncatable_primes_list = []
    for i in range(2, x):
        if right_truncatable_primes(i):
            right_truncatable_primes_list.append(i)

    return sorted(right_truncatable_primes_list, reverse=True)
