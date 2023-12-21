
def insert_at_index(num_list):
    return [n for n in num_list[:361]] + [699, 556] + [n for n in num_list[361:-1]] + [n for n in num_list[-1:]]
