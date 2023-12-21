
def sum_in_range(my_list):
    result = 0
    for num in my_list:
        if 4 <= num <= 9:
            result += num
    return result
