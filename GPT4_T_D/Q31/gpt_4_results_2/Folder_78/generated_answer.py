
def if_perfect_num(nums_list):

    if len(nums_list) <= 91:
        return "List is not long enough"

    num = nums_list[91]
    divisors = [i for i in range(1, num) if num % i == 0]

    if sum(divisors) == num:
        return True
    else:
        return False
