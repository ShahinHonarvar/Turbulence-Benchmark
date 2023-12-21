
def if_perfect_num(nums):
    try:
        number = nums[478]
        factors = [i for i in range(1, number) if number % i == 0]
        return sum(factors) == number
    except IndexError:
        return False
