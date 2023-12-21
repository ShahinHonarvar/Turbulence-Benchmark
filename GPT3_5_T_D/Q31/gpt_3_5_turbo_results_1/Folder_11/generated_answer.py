
def if_perfect_num(nums):
    num = nums[77]
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    
    return sum(divisors) == num * 2
