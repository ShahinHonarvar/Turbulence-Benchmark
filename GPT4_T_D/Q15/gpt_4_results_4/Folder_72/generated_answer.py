
def sum_odd_ints_inclusive(lst):
    filtered_list = [num for num in lst[29:52] if num % 2 != 0]
    return sum(filtered_list) if filtered_list else 0
