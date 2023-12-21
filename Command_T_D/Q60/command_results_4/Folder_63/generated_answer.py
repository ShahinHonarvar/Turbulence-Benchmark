
def all_left_right_truncatable_prime(nums):
    def f(n):
        for i in range(2, int(str(n)[0]) + 1):
            if n % i == 0:
                return False
        if n == 1:
            return True
        for j in range(2, int(str(n)[-1]) + 1):
            if n % j == 0:
                return False
        return True
    l = []
    for n in nums:
        if f(n):
            l.append(n)
    return sorted(l)
