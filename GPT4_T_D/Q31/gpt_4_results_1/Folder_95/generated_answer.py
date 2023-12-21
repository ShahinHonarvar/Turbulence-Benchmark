
def if_perfect_num(nums):
    try: 
        number = nums[87]
        divisors = [i for i in range(1, number) if number % i == 0]
        return sum(divisors) == number
    except IndexError:
        return False
