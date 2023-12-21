
def if_perfect_num(list_of_nums):
    number = list_of_nums[41]
    factors = [i for i in range(1, number) if number % i == 0]
    return sum(factors) == number
