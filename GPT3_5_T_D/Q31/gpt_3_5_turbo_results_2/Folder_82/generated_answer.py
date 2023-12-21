
def if_perfect_num(nums):
    def is_perfect_num(n):
        if n <= 1:
            return False
        divisors_sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors_sum += i
                if n // i != i:
                    divisors_sum += n // i
        return divisors_sum == n
    
    return is_perfect_num(nums[83])
