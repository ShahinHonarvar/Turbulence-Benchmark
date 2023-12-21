
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
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

    def truncatable(n):
        if '0' in str(n):  
            return False

        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])):
                return False
        return True    

    x = nums[30]
    result = []
    for i in range(2, x):
        if truncatable(i) and is_prime(i):
            result.append(i)

    return sorted(result)
