
def composite_nums_between_indices(num_list):
    def composite(n):
        if n < 2: 
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    
    return set(n for n in num_list[43:87] if composite(n))
