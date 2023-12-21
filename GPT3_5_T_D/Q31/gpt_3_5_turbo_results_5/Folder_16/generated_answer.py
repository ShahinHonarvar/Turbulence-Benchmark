
def if_perfect_num(nums):
    def is_perfect_num(num):
        divisors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors.append(i)
                divisors.append(num // i)
        divisors = list(set(divisors))
        return sum(divisors) == num

    if len(nums) > 162:
        return is_perfect_num(nums[162])
    else:
        return False
