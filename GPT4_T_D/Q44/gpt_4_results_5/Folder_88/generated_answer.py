
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2: 
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set([item for item in num_list[8:10] if is_composite(item)])
