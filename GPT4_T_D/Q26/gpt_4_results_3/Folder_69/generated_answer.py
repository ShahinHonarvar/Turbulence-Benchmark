
def sum_in_range(lst):
    filtered_list = [i for i in lst if 739 <= i <= 928]
    return sum(filtered_list) if filtered_list else 0
