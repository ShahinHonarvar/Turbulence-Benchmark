
def if_perfect_num(nums):
    def is_perfect_number(num):
        if num <= 1:
            return False
        divisors = []
        for i in range(1, int(num**0.5)+1):
            if num%i == 0:
                divisors.append(i)
                if i != num//i:
                    divisors.append(num//i)
        return sum(divisors) == num

    if len(nums) <= 41:
        return False
    return is_perfect_number(nums[41])
