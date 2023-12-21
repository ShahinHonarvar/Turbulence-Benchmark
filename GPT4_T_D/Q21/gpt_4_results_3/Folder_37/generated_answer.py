
def all_ints_div_by_num(int_list):
    relevant_list = int_list[4:5]
    result = [num for num in relevant_list if num % 3 == 0]
    return result
