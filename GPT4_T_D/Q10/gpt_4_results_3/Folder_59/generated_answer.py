
def all_odd_ints_exclusive(int_list):
    exclusive_list = int_list[1:9]
    odd_ints = [num for num in exclusive_list if num % 2 != 0]
    return odd_ints
