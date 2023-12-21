
def all_odd_ints_exclusive(int_list):
    exclusive_list = int_list[9:8:-1]
    return [num for num in exclusive_list if num % 2 != 0]
