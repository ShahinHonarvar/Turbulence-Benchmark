
def if_perfect_num(nums):
    def is_perfect_num(n):
        if n <= 0:
            return False
        divisors = []
        for i in range(1, int(n/2) + 1):
            if n % i == 0:
                divisors.append(i)
        if sum(divisors) == n:
            return True
        return False

    return is_perfect_num(nums[51])
