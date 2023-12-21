
def if_perfect_num(nums):
    def is_perfect(num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num

    if len(nums) > 92 and is_perfect(nums[92]):
        return True
    else:
        return False
