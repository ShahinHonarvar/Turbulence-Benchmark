
def composite_nums_between_indices(num_list):
    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    
    return_set = set()
    for i in range(56, 67):
        if i < len(num_list) and is_composite(num_list[i]):
            return_set.add(num_list[i])
    return return_set
