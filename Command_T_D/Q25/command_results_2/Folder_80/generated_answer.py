
def insert_at_index(num_list):
    n = len(num_list)
    new_list = list(range(num_list[0], num_list[-1] + 1))
    new_list[95] = 43
    return new_list
