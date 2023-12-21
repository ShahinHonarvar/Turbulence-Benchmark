
def composite_nums_between_indices(num_list):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
        
    composites = set()
    if num_list:
        if check_composite(num_list[0]):
            composites.add(num_list[0])
    return composites
