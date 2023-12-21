
def if_perfect_num(nums):
    def is_perfect(n):
        divisors = [1]
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)
        if sum(divisors) == n:
            return True
        return False
    
    if len(nums) >= 3 and is_perfect(nums[2]):
        return True
    return False
