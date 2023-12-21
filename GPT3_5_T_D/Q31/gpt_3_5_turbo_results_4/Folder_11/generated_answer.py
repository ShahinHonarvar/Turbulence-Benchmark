
def if_perfect_num(nums):
    def is_perfect(num):
        factors_sum = 1
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                factors_sum += i
                factors_sum += num // i
        if num != 1 and num**0.5 == int(num**0.5):
            factors_sum -= int(num**0.5)
        return factors_sum == num

    return is_perfect(nums[77])
