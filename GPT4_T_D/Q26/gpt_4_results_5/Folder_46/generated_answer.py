
def sum_in_range(lst):
    filtered_list = [num for num in lst if -616 <= num <= -205]
    return sum(filtered_list) if filtered_list else 0
