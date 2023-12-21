
def sum_ints_div_by_either_nums(num_list):
    relevant_nums = num_list[42:88]
    filtered_nums = [i for i in relevant_nums if i % -90 == 0 or i % -74 == 0]
    return sum(filtered_nums) if filtered_nums else 0
