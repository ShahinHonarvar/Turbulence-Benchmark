
def composite_nums_between_indices(nums_list):
    def is_composite(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return set(num for i, num in enumerate(nums_list[533:606]) if is_composite(num))
