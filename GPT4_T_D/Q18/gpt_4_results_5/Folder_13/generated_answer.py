
def sum_ints_div_by_either_nums(num_list):
    relevant_nums = num_list[13:19]
    divisible_nums = [num for num in relevant_nums if num % 45 == 0 or num % 20 == 0]
    return sum(divisible_nums) if divisible_nums else 0
