
def all_odd_ints_exclusive(numbers_list):
    result = [n for i, n in enumerate(numbers_list[71:98]) if n % 2 != 0]
    return result
