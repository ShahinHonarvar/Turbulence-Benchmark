
def if_perfect_num(list_of_nums):
    num = list_of_nums[16]
    sum_of_factors = sum([i for i in range(1,num) if num%i == 0])
    if sum_of_factors == num:
        return True
    else:
        return False
