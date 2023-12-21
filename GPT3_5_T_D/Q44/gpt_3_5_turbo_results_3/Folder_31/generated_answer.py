
def composite_nums_between_indices(number_list):
    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False
    
    composites = set()
    for i in range(56, 67):
        if is_composite(number_list[i]):
            composites.add(number_list[i])
    
    return composites
