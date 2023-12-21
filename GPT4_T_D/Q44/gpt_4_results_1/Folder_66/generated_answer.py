
def composite_nums_between_indices(num_list):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    
    composite_nums = set()
    
    for i in range(62, min(64, len(num_list))):
        if check_composite(num_list[i]):
            composite_nums.add(num_list[i])
    
    return composite_nums
